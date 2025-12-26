import pickle
import pandas as pd
import os

MODEL_PATH = "ml/phishing_model.pkl"

# Load model once
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("ML model not found. Train the model first.")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def extract_features(url: str):
    """
    Feature extraction must match training features
    """
    return {
        "url_length": len(url),
        "has_https": int(url.startswith("https")),
        "has_ip": int(any(char.isdigit() for char in url.split("/")[2])),
        "count_dots": url.count("."),
        "count_hyphens": url.count("-"),
        "has_at": int("@" in url),
    }


def predict_phishing_ml(url: str):
    features = extract_features(url)

    # FIX: use DataFrame with correct column names
    X = pd.DataFrame([features], columns=model.feature_names_in_)

    prediction = model.predict(X)[0]
    confidence = model.predict_proba(X)[0][1]

    return prediction, round(float(confidence), 2)

