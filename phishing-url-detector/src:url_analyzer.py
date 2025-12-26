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


















































  UW PICO 5.09                                                                                                      File: src/url_analyzer.py                                                                                                       Modified  

from rules import (
    check_ip_address,
    check_url_length,
    check_at_symbol,
    check_multiple_dots,
    check_http,
    check_phishing_keywords
)

def analyze_url(url):
    score = 0
    reasons = []

    if check_ip_address(url):
        score += 2
        reasons.append("Uses IP address instead of domain")

    if check_url_length(url):
        score += 1
        reasons.append("URL is very long")

    if check_at_symbol(url):
        score += 2
        reasons.append("Contains '@' symbol")

    if check_multiple_dots(url):
        score += 1
        reasons.append("Too many subdomains")

    if check_http(url):
        score += 1
        reasons.append("Uses HTTP instead of HTTPS")

    if check_phishing_keywords(url):
        score += 2
        reasons.append("Contains phishing keywords")

    return score, reasons
































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
