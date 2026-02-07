import requests
from urllib.parse import urljoin

XSS_PAYLOAD = "<script>alert('XSS')</script>"


def scan_xss(url, form):
    data = {}
    for input in form['inputs']:
        if input['type'] == 'text' and input['name']:
            data[input['name']] = XSS_PAYLOAD

    target = urljoin(url, form['action'])
    response = requests.post(target, data=data, timeout=10, verify=False)

    return XSS_PAYLOAD in response.text