from threat_intel import check_virustotal
from url_analyzer import analyze_url
from report_generator import generate_report
from ml_detector import predict_phishing_ml

DATA_FILE = "data/urls.txt"

def main():
    with open(DATA_FILE, "r") as file:
        urls = file.readlines()

    results = []

    for url in urls:
        url = url.strip()
        if not url:
            continue

        score, reasons = analyze_url(url)

        # Heuristic output
        if score >= 3:
            status = "SUSPICIOUS"
            print(f"[SUSPICIOUS] {url} (Score: {score})")
        else:
            status = "SAFE"
            print(f"[SAFE] {url} (Score: {score})")

        # ML inference
        ml_label, ml_confidence = predict_phishing_ml(url)

        if ml_label == 1:
            print(f"[ML] PHISHING (Confidence: {ml_confidence})")
        else:
            print(f"[ML] SAFE (Confidence: {ml_confidence})")

        # VirusTotal
        vt_result = check_virustotal(url)

        if vt_result:
            print(f"[VT] Malicious: {vt_result['malicious']} | Suspicious: {vt_result['suspicious']}")
        else:
            print("[VT] No data / API limit")

        print("-" * 40)

        results.append({
            "url": url,
            "score": score,
            "status": status,
            "reasons": reasons,
            "ml_prediction": "PHISHING" if ml_label == 1 else "SAFE",
            "ml_confidence": ml_confidence,
            "vt_result": vt_result
        })

    generate_report(results)

if __name__ == "__main__":
    main()


