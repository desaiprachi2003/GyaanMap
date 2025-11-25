# app_fastapi.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow React (localhost:3000)
    allow_credentials=True,
    allow_methods=["*"],       # IMPORTANT → allows OPTIONS
    allow_headers=["*"],
)


# Load models (same as in inference.py)
xgb = joblib.load("xgb_model.joblib")
le = joblib.load("label_encoder.joblib")
careers = pd.read_csv("careers_clean.csv")
embeddings = np.load("career_embeddings.npy")
sbert_meta = joblib.load("sbert_meta.joblib")
sbert = SentenceTransformer(sbert_meta["model_name"])

# load faiss if available else sklearn
try:
    import faiss
    faiss_index = faiss.read_index("career_faiss.index")
    use_faiss = True
except:
    from sklearn.neighbors import NearestNeighbors
    nn = NearestNeighbors(n_neighbors=10, metric="cosine").fit(embeddings)
    use_faiss = False

class QuizAnswers(BaseModel):
    answers: dict  # { "Q1":"A", "Q2":"B", ... }
    free_text: str = None  # optional

@app.post("/predict")
def predict(data: QuizAnswers):
    answers = data.answers
    # Convert answers -> features (re-use code from inference.py)
    def answers_to_features(answers):
        opt2cat = {"A":"tech","B":"creative","C":"management","D":"research","E":"sports","F": "social" }
        cats = ["tech","creative","management","research","sports","social"]
        cnts = {f"cnt_{c}":0 for c in cats}
        for q,v in answers.items():
            v = str(v).strip().upper()
            if v in opt2cat:
                cnts[f"cnt_{opt2cat[v]}"] += 1
        cnts_df = pd.DataFrame([cnts])
        total = cnts_df.sum(axis=1).iloc[0]
        pct = cnts_df.div(total if total>0 else 1, axis=0).add_prefix("pct_")
        X = pd.concat([cnts_df, pct], axis=1)
        return X
    X = answers_to_features(answers)
    pred_enc = xgb.predict(X.values)[0]
    pred_label = le.inverse_transform([pred_enc])[0]

    # Use free_text if provided, else prototype
    if data.free_text:
        query_text = data.free_text
    else:
        prototypes = {
            "tech": "I enjoy coding, debugging, building software and solving logical problems.",
            "creative": "I enjoy designing, drawing, storytelling, and producing creative content.",
            "management": "I enjoy leading teams, planning, organizing and managing people.",
            "research": "I enjoy experimenting, learning deeply, and doing scientific research.",
            "sports": "I enjoy physical activity, coaching and sports performance.",
            "social": "I enjoy helping people, communicating, supporting others, and community activities."
        }
        query_text = prototypes.get(pred_label, "")

    q_emb = sbert.encode([query_text], convert_to_numpy=True)
    q_emb_norm = q_emb / (np.linalg.norm(q_emb, axis=1, keepdims=True) + 1e-10)

    if use_faiss:
        D, I = faiss_index.search(q_emb_norm, 5)
    else:
        dists, I = nn.kneighbors(q_emb, n_neighbors=5)

    suggestions = []
    for idx in I[0]:
        row = careers.iloc[idx]
        suggestions.append({"id":int(row["career_id"]), "title":row["title"], "description":row["description"], "category": row["category"]})
    return {"predicted_category": pred_label, "suggestions": suggestions}

# keep this at the very end
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app_fastapi:app", host="127.0.0.1", port=8000, reload=True)
