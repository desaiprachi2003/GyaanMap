# generate_and_train_dataset.py
import random
import numpy as np
import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

random.seed(42)
np.random.seed(42)

OUT_DIR = os.getcwd()  # change if you want another folder

NUM_SAMPLES = 500
NUM_QUESTIONS = 25

# RIASEC types
RIA = ["Realistic", "Investigative", "Artistic", "Social", "Enterprising", "Conventional"]

# QUESTION -> RIASEC mapping (you can edit to match your QuizQuestions.pdf)
# This mapping is balanced but you can tweak distribution by repeating types more.
base = ["Investigative", "Investigative", "Artistic", "Social", "Enterprising", "Conventional", "Realistic"]
q_to_ria = [base[i % len(base)] for i in range(NUM_QUESTIONS)]

# Broad engineering career map (dominant RIASEC -> broad engineering field)
career_map = {
    "Realistic": "Mechanical Engineering",
    "Investigative": "Data / AI Engineering",
    "Artistic": "Design & UI/UX Engineering",
    "Social": "Civil Engineering",
    "Enterprising": "Electronics & Communication Engineering",
    "Conventional": "Software Engineering"
}

rows = []
for _ in range(NUM_SAMPLES):
    # pick a latent dominant type (weighted to create variety)
    dominant = random.choices(RIA, weights=[1.0,1.4,0.8,0.9,1.0,1.1], k=1)[0]
    responses = {}
    ria_scores = dict.fromkeys(RIA, 0)
    # generate Likert 1-5 answers with bias towards 'dominant' on mapped questions
    for i, qtype in enumerate(q_to_ria, start=1):
        if qtype == dominant:
            val = int(np.clip(round(np.random.normal(4, 0.8)), 1, 5))
        else:
            val = int(np.clip(round(np.random.normal(3, 1.0)), 1, 5))
        # occasional random flip for noise
        if random.random() < 0.05:
            val = random.randint(1, 5)
        responses[f"Q{i}"] = val
        ria_scores[qtype] += val
    # determine top type (introduce some ambiguity sometimes)
    sorted_scores = sorted(ria_scores.items(), key=lambda x: x[1], reverse=True)
    top_type = sorted_scores[0][0]
    if random.random() < 0.15 and len(sorted_scores) > 1:
        top_type = sorted_scores[1][0]
    label = career_map[top_type]
    row = responses.copy()
    row.update(ria_scores)
    row["Predicted_Career"] = label
    rows.append(row)

df = pd.DataFrame(rows)

# Add percentage columns (pct_<type>)
for t in RIA:
    df[f"pct_{t}"] = df[t] / df[[*RIA]].sum(axis=1)

# Reorder columns: Q1..Q25, RIA counts, pct columns, label
qcols = [f"Q{i}" for i in range(1, NUM_QUESTIONS+1)]
cnt_cols = RIA
pct_cols = [f"pct_{t}" for t in RIA]  
final_cols = qcols + cnt_cols + pct_cols + ["Predicted_Career"]
df = df[final_cols]

# Save full dataset
full_csv = os.path.join(OUT_DIR, "X_full.csv")
df.to_csv(full_csv, index=False)
print("Saved full dataset:", full_csv)

# Prepare X, y (features: cnt + pct)
X = df[cnt_cols + pct_cols].copy()
y = df["Predicted_Career"].copy()

# Save X.csv / y.csv (these match earlier pipeline)
X.to_csv(os.path.join(OUT_DIR, "X.csv"), index=False)
y.to_csv(os.path.join(OUT_DIR, "y.csv"), index=False, header=["label"])
print("Saved X.csv and y.csv")

# Split into training / testing Excel files (80/20)
train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)
train_xlsx = os.path.join(OUT_DIR, "career_training_data.xlsx")
test_xlsx = os.path.join(OUT_DIR, "career_testing_data.xlsx")
train_df.to_excel(train_xlsx, index=False)
test_df.to_excel(test_xlsx, index=False)
print("Saved Excel files:", train_xlsx, test_xlsx)

# TRAIN a quick XGBoost classifier so you have a model and metrics
le = LabelEncoder()
y_enc = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42, stratify=y_enc)

model = XGBClassifier(
    objective="multi:softprob",
    num_class=len(le.classes_),
    eval_metric="mlogloss",
    n_estimators=150,
    max_depth=4,
    learning_rate=0.1,
    random_state=42,
    use_label_encoder=False
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
labels = unique_labels(y_test, y_pred)
print("Model accuracy on synthetic test set:", round(labels, 2))
print("\nClassification report:\n")
print(classification_report(y_test, y_pred, labels=labels, target_names=le.classes_[labels]))

print("\nConfusion matrix:\n")
print(confusion_matrix(y_test, y_pred, labels=labels))


# Save model artifacts for inference.py compatibility
joblib.dump(model, os.path.join(OUT_DIR, "xgb_model.joblib"))
joblib.dump(le, os.path.join(OUT_DIR, "label_encoder.joblib"))
print("Saved model and label encoder.")

# Save a simple careers_clean.csv and placeholder SBERT artifacts so your existing inference.py runs.
careers_clean = pd.DataFrame({
    "career_id": list(range(len(le.classes_))),
    "title": le.inverse_transform(range(len(le.classes_))),
    "category": ["engineering"]*len(le.classes_),
    "description": le.inverse_transform(range(len(le.classes_)))
})
careers_clean.to_csv(os.path.join(OUT_DIR, "careers_clean.csv"), index=False)

# Create dummy embeddings to let inference run (replace with real SBERT embeddings later if needed)
embeddings = np.random.RandomState(42).rand(len(le.classes_), 384).astype(np.float32)
np.save(os.path.join(OUT_DIR, "career_embeddings.npy"), embeddings)
joblib.dump({"model_name": "sentence-transformers/paraphrase-MiniLM-L6-v2"}, os.path.join(OUT_DIR, "sbert_meta.joblib"))

print("Saved careers_clean.csv, career_embeddings.npy, sbert_meta.joblib")
print("\nAll files created in:", OUT_DIR)
