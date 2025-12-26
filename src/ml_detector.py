import pandas as pd
import joblib
from urllib.parse import urlparse

model = joblib.load("ml/phishing_model.pkl")

def extract_features(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    return [
        len(url),                                   # url_length
        int(any(char.isdigit() for char in hostname)),  # has_ip
        int(url.startswith("https")),               # has_https
        hostname.count('.') - 1 if hostname else 0, # subdomain_count
        int(any(word in url.lower() for word in ["login", "verify", "secure", "bank", "free", "gift"]))
    ]

def predict_phishing_ml(url):
    features = extract_features(url)

    df = pd.DataFrame([features], columns=[
        "url_length",
        "has_ip",
        "has_https",
        "subdomain_count",
        "has_suspicious_words"
    ])

    prediction = model.predict(df)[0]
    confidence = max(model.predict_proba(df)[0])

    return prediction, round(confidence, 2)

