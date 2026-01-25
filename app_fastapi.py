
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

import os
import json
import requests
from dotenv import load_dotenv
import time 


# =========================================================
# APP CONFIG
# =========================================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# LOAD ML MODELS (CAREER PREDICTION)
# =========================================================

xgb = joblib.load("xgb_model.joblib")
le = joblib.load("label_encoder.joblib")

careers = pd.read_csv("careers_clean.csv")
embeddings = np.load("career_embeddings.npy")

sbert_meta = joblib.load("sbert_meta.joblib")
sbert = SentenceTransformer(sbert_meta["model_name"])

try:
    import faiss
    faiss_index = faiss.read_index("career_faiss.index")
    use_faiss = True
except:
    from sklearn.neighbors import NearestNeighbors
    nn = NearestNeighbors(n_neighbors=10, metric="cosine").fit(embeddings)
    use_faiss = False


# =========================================================
# REQUEST MODELS
# =========================================================

class QuizAnswers(BaseModel):
    answers: dict
    free_text: str | None = None


class RoadmapRequest(BaseModel):
    career: str


class RoadmapResponse(BaseModel):
    career: str
    roadmap: list
    source: str


# =========================================================
# CAREER PREDICTION API
# =========================================================

@app.post("/predict")
def predict(data: QuizAnswers):

    def answers_to_features(answers):
        opt2cat = {
            "A": "tech",
            "B": "creative",
            "C": "management",
            "D": "research",
            "E": "sports",
            "F": "social"
        }

        cats = list(opt2cat.values())
        cnts = {f"cnt_{c}": 0 for c in cats}

        for v in answers.values():
            v = str(v).strip().upper()
            if v in opt2cat:
                cnts[f"cnt_{opt2cat[v]}"] += 1

        cnts_df = pd.DataFrame([cnts])
        total = cnts_df.sum(axis=1).iloc[0]
        pct = cnts_df.div(total if total else 1, axis=0).add_prefix("pct_")

        return pd.concat([cnts_df, pct], axis=1)

    X = answers_to_features(data.answers)
    pred_enc = xgb.predict(X.values)[0]
    pred_label = le.inverse_transform([pred_enc])[0]

    prototypes = {
        "tech": "I enjoy coding, debugging and solving logical problems.",
        "creative": "I enjoy design, art and creative expression.",
        "management": "I enjoy leading teams and organizing work.",
        "research": "I enjoy experiments and deep learning.",
        "sports": "I enjoy physical activity and coaching.",
        "social": "I enjoy helping people and community work."
    }

    query_text = data.free_text or prototypes.get(pred_label, "")
    q_emb = sbert.encode([query_text], convert_to_numpy=True)
    q_emb_norm = q_emb / (np.linalg.norm(q_emb, axis=1, keepdims=True) + 1e-10)

    if use_faiss:
        _, I = faiss_index.search(q_emb_norm, 5)
    else:
        _, I = nn.kneighbors(q_emb, n_neighbors=5)

    suggestions = []
    for idx in I[0]:
        row = careers.iloc[idx]
        suggestions.append({
            "id": int(row["career_id"]),
            "title": row["title"],
            "description": row["description"],
            "category": row["category"]
        })

    return {
        "predicted_category": pred_label,
        "suggestions": suggestions
    }


# =========================================================
# ROADMAP GENERATOR (HF + CACHE)
# =========================================================

CACHE_FILE = "roadmap_cache.json"
CACHE_TTL_SECONDS = 7 * 24 * 60 * 60  # 7 days

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN missing in .env file")

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)

        # 🔹 TTL validation
        meta = cache.get("_meta")
        if meta:
            last_updated = meta.get("last_updated", 0)
            age = time.time() - last_updated

            if age > CACHE_TTL_SECONDS:
                print("🕒 Cache expired. Ignoring old roadmap links.")
                return {}

        return cache

    except json.JSONDecodeError:
        return {}


def save_cache(cache):
    # 🔹 preserve existing metadata
    if "_meta" not in cache:
        cache["_meta"] = {}

    cache["_meta"]["last_updated"] = int(time.time())

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def safe_link(title: str, link: str | None):
    """
    Priority:
    1. Valid AI-provided link
    2. YouTube free learning video
    3. Google search (project-safe fallback)
    """

    # 1️⃣ Use AI link if valid
    if link:
        link = link.strip()
        if link.startswith("http"):
            return link

    # 2️⃣ YouTube fallback
    yt_query = title.replace(" ", "+") + "+tutorial"
    return f"https://www.youtube.com/results?search_query={yt_query}"




def parse_roadmap(text):
    roadmap = []
    current = None

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        if line.startswith("LEVEL:"):
            current = {"level": line.replace("LEVEL:", "").strip(), "topics": []}
            roadmap.append(current)

        elif line.startswith("TOPIC:") and current:
            raw = line.replace("TOPIC:", "").strip()

            if " | " in raw:
                title, link = raw.split(" | ", 1)
                link = safe_link(title, link)
            else:
                title = raw
                link = safe_link(title, None)

            current["topics"].append({
            "title": title.strip(),
            "link": link
})


    return roadmap


def build_ui_roadmap(parsed):
    durations = {
        "Foundation": "3–6 months",
        "Intermediate": "6–12 months",
        "Advanced": "12–18 months",
        "Projects": "18+ months"
    }

    ui = []

    for r in parsed:
        ui.append({
            "level": r["level"],
            "duration": durations.get(r["level"], "—"),
            "topics": [
                {
                    "title": t["title"],
                    "link": t["link"]
                }
                for t in r["topics"]
            ]
        })

    return ui



def generate_roadmap_from_hf(career_name):
    prompt = f"""
Create a beginner-friendly learning roadmap for the career: {career_name}.

RULES:
- Plain text only
- No numbering
- Use this format exactly

LEVEL: Foundation
TOPIC: topic | link

LEVEL: Intermediate
TOPIC: topic | link

LEVEL: Advanced
TOPIC: topic | link

LEVEL: Projects
TOPIC: topic
"""

    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
    response.raise_for_status()

    text = response.json()["choices"][0]["message"]["content"]
    return build_ui_roadmap(parse_roadmap(text))


# =========================================================
# ROADMAP API ENDPOINT
# =========================================================

@app.post("/roadmap", response_model=RoadmapResponse)
def get_roadmap(data: RoadmapRequest):

    career = data.career.strip()
    if not career:
        raise HTTPException(status_code=400, detail="Career name required")

    cache = load_cache()
  

# 🔹 ignore metadata key
    if career in cache and career != "_meta":
        return {
        "career": career,
        "roadmap": cache[career]["roadmap"],
        "source": "cache"
        }

     

    roadmap = generate_roadmap_from_hf(career)

    cache[career] = {
        "career": career,
        "roadmap": roadmap
    }

    save_cache(cache)

    return {
        "career": career,
        "roadmap": roadmap,
        "source": "hf"
    }


# =========================================================
# RUN SERVER
# =========================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app_fastapi:app", host="127.0.0.1", port=8000, reload=True)
