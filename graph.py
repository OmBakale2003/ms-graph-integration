import requests
from auth import get_graph_token

def fetch_users():
    token = get_graph_token()

    url = "https://graph.microsoft.com/v1.0/users"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()