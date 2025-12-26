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

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

DEBUG: URLs read from file → ['http://192.168.1.10/login\n', 'https://secure-paypal.com.verify.account-update.ru\n', 'https://google.com\n', 'http://free-gift-login.com\n', '\n']
[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
[SAFE] https://google.com (Score: 0)
[SUSPICIOUS] http://free-gift-login.com (Score: 3)

Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 20
    urls = file.readlines())
                           ^
SyntaxError: unmatched ')'
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py


  UW PICO 5.09                                                                                                            File: main.py                                                                                                             Modified  

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

































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
