import requests
import extbase

def server_power(payload, signal):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/power'
    cmd = {
        'signal': signal
    }
    response = requests.request('POST', url_value, json=cmd, headers=extbase.entrance(payload))
    result = response.text
    return result

def send_command(payload, command):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/command'
    cmd = {
        'command': command
    }
    response = requests.request('POST', url_value, json=cmd, headers=extbase.entrance(payload))
    result = response.text
    return result

def consol_details(payload):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/websocket'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def resources_usage(payload):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/resources'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def server_details(payload):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def server_list(payload):
    url, _, _ = extbase.keys(payload)
    url_value = f'{url}/api/client'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def show_premission(payload):
    url, _, _, = extbase.keys(payload)
    url_value = f'{url}/api/client/permissions'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def account_details(payload):
    url, _, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/account'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def file_list(payload):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/files/list'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def file_usage(payload, pyt):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/files/{pyt}'
    response = requests.request('GET', url_value, headers=extbase.entrance(payload))
    result = response.text
    return result

def file_rename(payload, name, newname):
    url, id, _ = extbase.keys(payload)
    url_value = f'{url}/api/client/servers/{id}/files/rename'
    cmd = {
        'root': '/',
        'files': [
            {
                "from": name,
                "to": newname
            }
        ]
    }
    response = requests.request('PUT', url_value, json=cmd, headers=extbase.entrance(payload))
    result = response.text
    return result








