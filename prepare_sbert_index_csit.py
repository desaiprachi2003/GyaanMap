import pandas as pd
import numpy as np
import joblib
from sentence_transformers import SentenceTransformer

# Optional FAISS
try:
    import faiss
    use_faiss = True
except ImportError:
    use_faiss = False

# -------------------------------------------------
# Load CS/IT careers
# -------------------------------------------------
df = pd.read_csv("careers_csit.csv")

texts = (
    df["title"] + ". " +
    df["description"] + ". Category: " +
    df["category"]
).tolist()

# -------------------------------------------------
# Load SBERT model
# -------------------------------------------------
MODEL_NAME = "all-MiniLM-L6-v2"
sbert = SentenceTransformer(MODEL_NAME)

embeddings = sbert.encode(
    texts,
    convert_to_numpy=True,
    normalize_embeddings=True
)

# -------------------------------------------------
# Save embeddings
# -------------------------------------------------
np.save("career_embeddings_csit.npy", embeddings)

joblib.dump(
    {"model_name": MODEL_NAME},
    "sbert_meta.joblib"
)

# -------------------------------------------------
# Build FAISS index (if available)
# -------------------------------------------------
if use_faiss:
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    faiss.write_index(index, "career_faiss_csit.index")
    print("✅ FAISS index created")
else:
    print("⚠️ FAISS not installed — fallback KNN will be used")

print("✅ SBERT embeddings ready:", embeddings.shape)
