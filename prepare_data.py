import pandas as pd
import sys
import os

if not os.path.exists("external.csv"):
    sys.exit("external.csv not found")

df = pd.read_csv("external.csv")
df = df.dropna(subset=["Suggested Job Role"])
X = df.drop(columns=["Suggested Job Role"])
y = df["Suggested Job Role"]
X = pd.get_dummies(X)
X.to_csv("X.csv", index=False)
y.to_csv("y.csv", index=False, header=["label"])
pd.concat([X, y], axis=1).to_csv("X_full.csv", index=False)
print("Saved X.csv, y.csv, X_full.csv")
