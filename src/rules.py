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

