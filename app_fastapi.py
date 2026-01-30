
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

# =========================================================
# LOAD CS/IT ML MODELS & DATA
# =========================================================

# XGBoost career classifier (CS/IT only)
xgb = joblib.load("xgb_model.joblib")
le = joblib.load("label_encoder.joblib")

# CS/IT careers metadata
careers = pd.read_csv("careers_csit.csv")

# SBERT embeddings for CS/IT careers
embeddings = np.load("career_embeddings_csit.npy")

# SBERT model metadata
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
    Q1: int
    Q2: int
    Q3: int
    Q4: int
    Q5: int
    Q6: int
    Q7: int
    Q8: int
    Q9: int
    Q10: int
    Q11: int
    Q12: int
    Q13: int
    Q14: int
    Q15: int
    Q16: int
    Q17: int
    Q18: int
    Q19: int
    Q20: int
    Q21: int
    Q22: int
    Q23: int
    Q24: int
    free_text: str | None = None

class RIASECInput(BaseModel):
    R: float
    I: float
    A: float
    S: float
    E: float
    C: float


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
def predict(data: RIASECInput):

    # 1️⃣ Build ML input (RIASEC → DataFrame)
    X = pd.DataFrame([{
        "R": data.R,
        "I": data.I,
        "A": data.A,
        "S": data.S,
        "E": data.E,
        "C": data.C
    }])

    # 2️⃣ Get probability scores from XGBoost
    probs = xgb.predict_proba(X)[0]   # (num_classes,)

    # 3️⃣ Pick TOP 3 careers
    top3_idx = np.argsort(probs)[-3:][::-1]

    top3 = [
        {
            "career": le.inverse_transform([idx])[0],
            "confidence": round(float(probs[idx]), 3)
        }
        for idx in top3_idx
    ]

    # 4️⃣ CS/IT-only intent prototypes (for SBERT)
    prototypes = {
        "Backend Developer": "I enjoy APIs, databases, and server-side systems.",
        "Frontend Developer": "I enjoy UI design and interactive web experiences.",
        "Data Scientist": "I enjoy data analysis, statistics, and machine learning.",
        "DevOps Engineer": "I enjoy CI/CD pipelines, cloud infrastructure, and automation.",
        "Cybersecurity Analyst": "I enjoy securing systems and analyzing vulnerabilities."
    }

    # 5️⃣ Use TOP career intent for semantic retrieval
    query_text = prototypes.get(top3[0]["career"], "")
    q_emb = sbert.encode([query_text], convert_to_numpy=True)
    q_emb_norm = q_emb / (np.linalg.norm(q_emb, axis=1, keepdims=True) + 1e-10)

    # 6️⃣ Retrieve similar careers/resources
    if use_faiss:
        _, I = faiss_index.search(q_emb_norm, 5)
    else:
        _, I = nn.kneighbors(q_emb, n_neighbors=5)

    suggestions = [
        {
            "id": int(careers.iloc[idx]["career_id"]),
            "title": careers.iloc[idx]["title"],
            "description": careers.iloc[idx]["description"],
            "category": careers.iloc[idx]["category"]
        }
        for idx in I[0]
    ]

    # 7️⃣ Final response
    return {
        "top_3_careers": top3,
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
