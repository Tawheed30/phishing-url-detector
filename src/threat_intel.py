import os
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")
VT_URL = "https://www.virustotal.com/api/v3/urls/"

def get_url_id(url):
    return hashlib.sha256(url.encode()).hexdigest()

def check_virustotal(url):
    if not VT_API_KEY:
        return None

    url_id = get_url_id(url)
    headers = {
        "x-apikey": VT_API_KEY
    }

    response = requests.get(VT_URL + url_id, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    stats = data["data"]["attributes"]["last_analysis_stats"]

    return {
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "harmless": stats.get("harmless", 0)
    }

