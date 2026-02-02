# dataverse.py
import requests
from auth import get_access_token
import config

def list_accounts(top: int = 10):
    token = get_access_token()
    url = f"{config.ENV_URL}/api/data/v9.2/accounts"
    params = {"$select": "name,accountnumber", "$top": str(top)}
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    }
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json().get("value", [])

def list_test_1(top: int = 5):
    """Fetch rows from the cr277_test_1 Dataverse table"""
    token = get_access_token()
    base = config.ENV_URL.rstrip('/')

    # Use the EXACT EntitySetName from metadata
    entity_set = "cr277_test_1s"
    url = f"{base}/api/data/v9.2/{entity_set}"

    params = {
        "$top": top,
        "$select": "cr277_source_timestamp,cr277_json_dump"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    }

    resp = requests.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()

    return resp.json().get("value", [])


def find_test_table():
    """Find exact EntitySetName for tables containing 'test' in LogicalName"""
    token = get_access_token()
    base = config.ENV_URL.rstrip('/')

    url = f"{base}/api/data/v9.2/EntityDefinitions?$select=LogicalName,EntitySetName,DisplayName"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    entities = resp.json().get("value", [])

    # Filter client-side
    matches = [
        e for e in entities
        if "test" in e["LogicalName"].lower()
    ]

    for table in matches:
        display = table.get("DisplayName", {}).get("LocalizedLabels", [])
        display_name = display[0]["Label"] if display else "N/A"

        print(f"Display: {display_name}")
        print(f"Logical: {table['LogicalName']}")
        print(f"API endpoint: {table['EntitySetName']}")
        print("---")

    return matches

# Update main.py temporarily:
# def main():


