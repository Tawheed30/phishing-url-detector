import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("ml/phishing_dataset.csv")

# Features (ORDER MATTERS — DO NOT CHANGE)
X = df[[
    "url_length",
    "has_ip",
    "has_https",
    "subdomain_count",
    "has_suspicious_words"
]]

# Label
y = df["label"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
joblib.dump(model, "ml/phishing_model.pkl")

print("✅ ML model trained and saved as phishing_model.pkl")

