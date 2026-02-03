import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("csit_riasec_interest_dataset.csv")

X = df[["R", "I", "A", "S", "E", "C"]]
y = df["interest_label"]

# ===============================
# ENCODE LABELS
# ===============================
le = LabelEncoder()
y_enc = le.fit_transform(y)

# ===============================
# TRAIN / TEST SPLIT
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_enc,
    test_size=0.2,
    random_state=42,
    stratify=y_enc
)

# ===============================
# XGBOOST MODEL
# ===============================
xgb = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.08,
    subsample=0.9,
    colsample_bytree=0.9,
    objective="multi:softprob",   # REQUIRED for top-k
    eval_metric="mlogloss",
    random_state=42
)

xgb.fit(X_train, y_train)

# ===============================
# EVALUATION
# ===============================
y_pred = xgb.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n MODEL ACCURACY:", round(acc * 100, 2), "%\n")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ===============================
# SAVE MODEL
# ===============================
joblib.dump(xgb, "xgb_model.joblib")
joblib.dump(le, "label_encoder.joblib")

print(" CS/IT XGBoost model trained & saved")
