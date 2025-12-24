Last login: Wed Dec 24 16:00:08 on ttys002
mohammedtawheed@Mohammeds-MacBook-Pro-2 mitre-soc-simulator % mkdir phishing-url-detector
cd phishing-url-detector

mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % mkdir data src reports
touch README.md requirements.txt .gitignore
touch data/sample_urls.txt
touch src/main.py src/url_analyzer.py src/rules.py src/report_generator.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 --version

Python 3.9.6
mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % Python 3.9+ 

zsh: command not found: Python
mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 --version

Python 3.9.6
mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 -m venv venv
source venv/bin/activate

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/rules.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/url_analyzer.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano data/sample_urls.txt

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/report_generator.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cat reports/phishing_report.txt

cat: reports/phishing_report.txt: No such file or directory
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cat reports/phishing_report.txt

cat: reports/phishing_report.txt: No such file or directory
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pwd
/Users/mohammedtawheed/mitre-soc-simulator/phishing-url-detector
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cd src
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % cd src

cd: no such file or directory: src
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano ../data/sample_urls.txt

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 8
    with open(DATA_FILE, "r") as file:
    ^
IndentationError: expected an indented block
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 3, in <module>
    from report_generator import generate_report
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/report_generator.py", line 1
    [PHISHING] http://192.168.1.10/login (Score: 6)
               ^
SyntaxError: invalid syntax
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano report_generator.py



  UW PICO 5.09                                                                                                      File: report_generator.py                                                                                                       Modified  

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













































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
