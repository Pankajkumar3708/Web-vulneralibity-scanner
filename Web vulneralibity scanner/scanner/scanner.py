from .crawler import get_forms, get_form_details
from .sqli import scan_sqli
from .xss import scan_xss
from .csrf import scan_csrf
from .headers import scan_headers
import json

def run_scan(url):
    results = {
        'url': url,
        'sql_injection': [],
        'xss': [],
        'csrf': [],
        'missing_headers': []
    }

    forms = get_forms(url)

    for form in forms:
        details = get_form_details(form)

        if scan_sqli(url, details):
            results['sql_injection'].append(details['action'])

        if scan_xss(url, details):
            results['xss'].append(details['action'])

        if scan_csrf(details):
            results['csrf'].append(details['action'])

    results['missing_headers'] = scan_headers(url)

    with open('reports/report.json', 'w') as f:
        json.dump(results, f, indent=4)

    return results