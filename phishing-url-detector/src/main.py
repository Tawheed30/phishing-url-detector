import os
from url_analyzer import analyze_url
from report_generator import generate_report

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "sample_urls.txt")

def classify_score(score):
    if score >= 6:
        return "PHISHING"
    elif score >= 3:
        return "SUSPICIOUS"
    else:
        return "SAFE"

def main():
    results = []

    with open(DATA_FILE, "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        score, reasons = analyze_url(url)
        status = classify_score(score)

        results.append((url, score, status, reasons))
        print(f"[{status}] {url} (Score: {score})")

    generate_report(results)
    print("\nReport saved to reports/phishing_report.txt")

if __name__ == "__main__":
    main()

