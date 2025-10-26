import pandas as pd
import numpy as np
import joblib
import os
from sentence_transformers import SentenceTransformer

if not os.path.exists("xgb_model.joblib") or not os.path.exists("label_encoder.joblib"):
    raise SystemExit("Train model first with train_xgb.py")

if not os.path.exists("careers_clean.csv") or not os.path.exists("career_embeddings.npy") or not os.path.exists("sbert_meta.joblib"):
    raise SystemExit("Run prepare_sbert_index.py first")

model = joblib.load("xgb_model.joblib")
le = joblib.load("label_encoder.joblib")
careers = pd.read_csv("careers_clean.csv")
embeddings = np.load("career_embeddings.npy")
sbert_meta = joblib.load("sbert_meta.joblib")
sbert = SentenceTransformer(sbert_meta["model_name"])

emb_norm = embeddings / (np.linalg.norm(embeddings, axis=1, keepdims=True) + 1e-10)

def predict_and_retrieve(x_row, top_k=5):
    pred_enc = model.predict([x_row])[0]
    pred_label = le.inverse_transform([pred_enc])[0]
    q_emb = sbert.encode([pred_label], convert_to_numpy=True)
    q_emb_norm = q_emb / (np.linalg.norm(q_emb, axis=1, keepdims=True) + 1e-10)
    sims = (emb_norm @ q_emb_norm.T).flatten()
    top_idx = np.argsort(-sims)[:top_k]
    results = []
    for idx in top_idx:
        row = careers.iloc[idx]
        results.append({"career_id": int(row["career_id"]), "title": row["title"], "description": row["description"]})
    return {"predicted_category": pred_label, "suggestions": results}

if __name__ == "__main__":
    X = pd.read_csv("X.csv")
    sample = X.iloc[0].tolist()
    print(predict_and_retrieve(sample, top_k=5))
