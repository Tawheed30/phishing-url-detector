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

