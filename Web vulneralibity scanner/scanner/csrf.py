
def scan_csrf(form):
    for input in form['inputs']:
        if input['type'] == 'hidden' and 'csrf' in (input['name'] or '').lower():
            return False
    return True
