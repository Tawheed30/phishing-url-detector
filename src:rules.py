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




















































  UW PICO 5.09                                                                                                          File: src/rules.py                                                                                                          Modified  

import re
from urllib.parse import urlparse

def check_ip_address(url):
    pattern = r'http[s]?://(?:\d{1,3}\.){3}\d{1,3}'
    return re.match(pattern, url) is not None

def check_url_length(url):
    return len(url) > 75

def check_at_symbol(url):
    return "@" in url

def check_multiple_dots(url):
    parsed = urlparse(url)
    return parsed.netloc.count('.') > 3

def check_http(url):
    return url.startswith("http://")

def check_phishing_keywords(url):
    keywords = [
        "login", "verify", "secure", "account",
        "update", "bank", "free", "signin"
    ]
    return any(word in url.lower() for word in keywords)












































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
