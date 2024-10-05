
def keys(payload):
    url = payload['url']
    id = payload['id']
    apikey = payload['apikey']
    return url, id, apikey

def entrance(payload):
    url, id, apikey = keys(payload)
    headers = {
        "Authorization": f"Bearer {apikey}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    return headers

