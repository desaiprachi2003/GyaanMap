# # app_fastapi.py
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
# import numpy as np
# import pandas as pd
# from sentence_transformers import SentenceTransformer
# from fastapi.middleware.cors import CORSMiddleware


# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],       # allow React (localhost:3000)
#     allow_credentials=True,
#     allow_methods=["*"],       # IMPORTANT → allows OPTIONS
#     allow_headers=["*"],
# )


# # Load models (same as in inference.py)
# xgb = joblib.load("xgb_model.joblib")
# le = joblib.load("label_encoder.joblib")
# careers = pd.read_csv("careers_clean.csv")
# embeddings = np.load("career_embeddings.npy")
# sbert_meta = joblib.load("sbert_meta.joblib")
# sbert = SentenceTransformer(sbert_meta["model_name"])

# # load faiss if available else sklearn
# try:
#     import faiss
#     faiss_index = faiss.read_index("career_faiss.index")
#     use_faiss = True
# except:
#     from sklearn.neighbors import NearestNeighbors
#     nn = NearestNeighbors(n_neighbors=10, metric="cosine").fit(embeddings)
#     use_faiss = False

# class QuizAnswers(BaseModel):
#     answers: dict  # { "Q1":"A", "Q2":"B", ... }
#     free_text: str = None  # optional

# @app.post("/predict")
# def predict(data: QuizAnswers):
#     answers = data.answers
#     # Convert answers -> features (re-use code from inference.py)
#     def answers_to_features(answers):
#         opt2cat = {"A":"tech","B":"creative","C":"management","D":"research","E":"sports","F": "social" }
#         cats = ["tech","creative","management","research","sports","social"]
#         cnts = {f"cnt_{c}":0 for c in cats}
#         for q,v in answers.items():
#             v = str(v).strip().upper()
#             if v in opt2cat:
#                 cnts[f"cnt_{opt2cat[v]}"] += 1
#         cnts_df = pd.DataFrame([cnts])
#         total = cnts_df.sum(axis=1).iloc[0]
#         pct = cnts_df.div(total if total>0 else 1, axis=0).add_prefix("pct_")
#         X = pd.concat([cnts_df, pct], axis=1)
#         return X
#     X = answers_to_features(answers)
#     pred_enc = xgb.predict(X.values)[0]
#     pred_label = le.inverse_transform([pred_enc])[0]

#     # Use free_text if provided, else prototype
#     if data.free_text:
#         query_text = data.free_text
#     else:
#         prototypes = {
#             "tech": "I enjoy coding, debugging, building software and solving logical problems.",
#             "creative": "I enjoy designing, drawing, storytelling, and producing creative content.",
#             "management": "I enjoy leading teams, planning, organizing and managing people.",
#             "research": "I enjoy experimenting, learning deeply, and doing scientific research.",
#             "sports": "I enjoy physical activity, coaching and sports performance.",
#             "social": "I enjoy helping people, communicating, supporting others, and community activities."
#         }
#         query_text = prototypes.get(pred_label, "")

#     q_emb = sbert.encode([query_text], convert_to_numpy=True)
#     q_emb_norm = q_emb / (np.linalg.norm(q_emb, axis=1, keepdims=True) + 1e-10)

#     if use_faiss:
#         D, I = faiss_index.search(q_emb_norm, 5)
#     else:
#         dists, I = nn.kneighbors(q_emb, n_neighbors=5)

#     suggestions = []
#     for idx in I[0]:
#         row = careers.iloc[idx]
#         suggestions.append({"id":int(row["career_id"]), "title":row["title"], "description":row["description"], "category": row["category"]})
#     return {"predicted_category": pred_label, "suggestions": suggestions}

# # keep this at the very end
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app_fastapi:app", host="127.0.0.1", port=8000, reload=True)
# **************************************************************************************************************************************8

# app_fastapi.py

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
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


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
            current["topics"].append(line.replace("TOPIC:", "").strip())

    return roadmap


def build_ui_roadmap(parsed):
    durations = {
        "Foundation": "3–6 months",
        "Intermediate": "6–12 months",
        "Advanced": "12–18 months",
        "Projects": "18+ months"
    }

    return [
        {
            "level": r["level"],
            "duration": durations.get(r["level"], "—"),
            "topics": r["topics"]
        }
        for r in parsed
    ]


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

    if career in cache:
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
