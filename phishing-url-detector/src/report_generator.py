import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_FILE = os.path.join(BASE_DIR, "reports", "phishing_report.txt")

def generate_report(results):
    with open(REPORT_FILE, "w") as report:
        report.write("PHISHING URL DETECTION REPORT\n")
        report.write("=" * 35 + "\n")
        report.write(f"Generated on: {datetime.now()}\n\n")

        for url, score, status, reasons in results:
            report.write(f"URL: {url}\n")
            report.write(f"Risk Score: {score}\n")
            report.write(f"Status: {status}\n")

            if reasons:
                report.write("Reasons:\n")
                for reason in reasons:
                    report.write(f"- {reason}\n")
            else:
                report.write("Reasons: None\n")

            report.write("-" * 35 + "\n")

