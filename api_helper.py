import requests
from auth import authenticate

BASE_URL = "https://sandbox-sdwan-2.cisco.com"

def get_device_inventory(session=None, headers=None):
    if session is None or headers is None:
        session, headers = authenticate()

    url = f"{BASE_URL}/dataservice/device"
    response = session.get(url, headers=headers, verify=False)

    try:
        devices = response.json().get("data", [])
    except ValueError:
        raise Exception("Failed to parse response JSON")

    return devices
