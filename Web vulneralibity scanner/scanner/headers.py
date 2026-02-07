import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

def scan_headers(url):
    try:
        response = requests.get(url, timeout=10, verify=False)
        missing = []

        for header in SECURITY_HEADERS:
            if header not in response.headers:
                missing.append(header)

        return missing

    except requests.exceptions.RequestException as e:
        print(f"[!] Header scan failed: {e}")
        return ["Unable to fetch headers"]
