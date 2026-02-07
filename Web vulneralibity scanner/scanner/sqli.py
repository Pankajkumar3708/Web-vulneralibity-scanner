import requests
from urllib.parse import urljoin

SQL_PAYLOADS = ["'", "' OR '1'='1", "\" OR \"1\"=\"1"]


def scan_sqli(url, form):
    vulnerable = False
    for payload in SQL_PAYLOADS:
        data = {}
        for input in form['inputs']:
            if input['name']:
                data[input['name']] = payload

        target = urljoin(url, form['action'])
        response = requests.post(target, data=data, timeout=10, verify=False)

        errors = ["sql", "syntax", "mysql", "query"]
        if any(err in response.text.lower() for err in errors):
            vulnerable = True
            break

    return vulnerable