import pandas as pd
import numpy as np
import joblib
import os
from sentence_transformers import SentenceTransformer

if not os.path.exists("external.csv"):
    raise SystemExit("external.csv not found")

df = pd.read_csv("external.csv")
df = df.dropna(subset=["Suggested Job Role"])
df_unique = df[["Suggested Job Role"]].drop_duplicates().reset_index(drop=True)
df_unique["career_id"] = df_unique.index
df_unique["title"] = df_unique["Suggested Job Role"]
df_unique["category"] = "career"
df_unique["description"] = df_unique["Suggested Job Role"]

model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

docs = (df_unique["title"].fillna("") + ". " + df_unique["description"].fillna("")).tolist()
embeddings = model.encode(docs, show_progress_bar=True, convert_to_numpy=True)

np.save("career_embeddings.npy", embeddings)
df_unique.to_csv("careers_clean.csv", index=False)
joblib.dump({"model_name": model_name}, "sbert_meta.joblib")
print("Saved careers_clean.csv, career_embeddings.npy, sbert_meta.joblib")
