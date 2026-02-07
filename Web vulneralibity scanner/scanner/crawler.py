import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_forms(url):
    try:
        response = requests.get(
            url,
            timeout=10,
            verify=False
        )
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find_all("form")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching {url}: {e}")
        return []


def get_form_details(form):
    details = {}
    details['action'] = form.attrs.get('action', '')
    details['method'] = form.attrs.get('method', 'get').lower()
    details['inputs'] = []

    for input_tag in form.find_all('input'):
        details['inputs'].append({
            'name': input_tag.attrs.get('name'),
            'type': input_tag.attrs.get('type', 'text'),
            'value': input_tag.attrs.get('value', '') 
        })
    return details
