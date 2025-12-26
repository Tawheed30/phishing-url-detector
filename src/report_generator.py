from datetime import datetime
import os

def generate_report(results):
    os.makedirs("reports", exist_ok=True)

    report_path = "reports/phishing_report.txt"

    with open(report_path, "w") as report:
        report.write("PHISHING URL DETECTION REPORT\n")
        report.write("=" * 40 + "\n")
        report.write(f"Generated on: {datetime.now()}\n\n")

        for item in results:
            report.write(f"URL: {item['url']}\n")
            report.write(f"Risk Score: {item['score']}\n")
            report.write(f"Status: {item['status']}\n")
            report.write(f"ML Prediction: {item['ml_prediction']}\n")
            report.write(f"ML Confidence: {item['ml_confidence']}\n")

            if item["reasons"]:
                report.write("Reasons:\n")
                for reason in item["reasons"]:
                    report.write(f"- {reason}\n")
            else:
                report.write("Reasons: None\n")

            report.write("-" * 40 + "\n")

    print("Report saved to reports/phishing_report.txt")

