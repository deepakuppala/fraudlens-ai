import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

print("Loading dataset...")

data = pd.read_csv("creditcard.csv")

# 🔥 TAKE SMALL SAMPLE (VERY IMPORTANT)
data = data.sample(20000, random_state=42)

print("Dataset reduced for fast training")

X = data.drop("Class", axis=1)
y = data["Class"]

model = RandomForestClassifier(
    class_weight="balanced",
    n_estimators=50   # reduce trees for speed
)

print("Training model...")
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained FAST and saved!")