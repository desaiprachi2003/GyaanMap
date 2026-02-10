# import pandas as pd
# import joblib
# from xgboost import XGBClassifier
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.utils import resample

# # ===============================
# # LOAD DATA
# # ===============================
# df = pd.read_csv("csit_riasec_interest_dataset.csv")

# # ===============================
# # UPSAMPLE ALL MINORITY CLASSES
# # ===============================
# # Find the size of the largest class
# max_size = df["interest_label"].value_counts().max()

# # Upsample each class to match the largest
# df_upsampled = pd.DataFrame()
# for label in df["interest_label"].unique():
#     df_label = df[df["interest_label"] == label]
#     df_label_upsampled = resample(
#         df_label,
#         replace=True,
#         n_samples=max_size,
#         random_state=42
#     )
#     df_upsampled = pd.concat([df_upsampled, df_label_upsampled])

# # Shuffle the dataset
# df_upsampled = df_upsampled.sample(frac=1, random_state=42).reset_index(drop=True)

# # ===============================
# # FEATURES & TARGET
# # ===============================
# X = df_upsampled[["R", "I", "A", "S", "E", "C"]]
# y = df_upsampled["interest_label"]

# # ===============================
# # ENCODE LABELS
# # ===============================
# le = LabelEncoder()
# y_enc = le.fit_transform(y)

# # ===============================
# # TRAIN / TEST SPLIT
# # ===============================
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y_enc,
#     test_size=0.2,
#     random_state=42,
#     stratify=y_enc
# )

# # ===============================
# # XGBOOST MODEL
# # ===============================
# xgb = XGBClassifier(
#     n_estimators=300,
#     max_depth=5,
#     learning_rate=0.08,
#     subsample=0.9,
#     colsample_bytree=0.9,
#     objective="multi:softprob",   # REQUIRED for top-k
#     eval_metric="mlogloss",
#     random_state=42
# )

# xgb.fit(X_train, y_train)

# # ===============================
# # EVALUATION
# # ===============================
# y_pred = xgb.predict(X_test)
# acc = accuracy_score(y_test, y_pred)

# print("\nMODEL ACCURACY:", round(acc * 100, 2), "%\n")
# print(classification_report(y_test, y_pred, target_names=le.classes_))

# # ===============================
# # SAVE MODEL
# # ===============================
# joblib.dump(xgb, "xgb_model.joblib")
# joblib.dump(le, "label_encoder.joblib")

# print("✅ CS/IT XGBoost model trained & saved (all classes balanced)")


#***********************************************************************************************************
#UPDATED CODE
#***********************************************************************************************************
import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ===============================
# LOAD FINAL DATASET
# ===============================
df = pd.read_csv("csit_riasec_interest_dataset_final.csv")

# ===============================
# FEATURES & TARGET
# ===============================
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
    objective="multi:softprob",
    eval_metric="mlogloss",
    random_state=42
)

xgb.fit(X_train, y_train)

# ===============================
# EVALUATION
# ===============================
y_pred = xgb.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\nFINAL MODEL ACCURACY:", round(acc * 100, 2), "%\n")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# ===============================
# SAVE FINAL MODEL
# ===============================
joblib.dump(xgb, "xgb_model_final.joblib")
joblib.dump(le, "label_encoder_final.joblib")

print("✅ FINAL XGBoost model trained & saved safely")
