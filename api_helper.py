import requests
from auth import authenticate

BASE_URL = "https://sandbox-sdwan-2.cisco.com"

def get_device_inventory(session=None, headers=None):
    if session is None or headers is None:
        session, headers = authenticate()

    url = f"{BASE_URL}/dataservice/device"
    response = session.get(url, headers=headers, verify=False)

    # ✅ Check for JSON response type
    content_type = response.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        raise Exception(f"Expected JSON but got: {content_type}\nResponse Text:\n{response.text}")

    try:
        return response.json().get("data", [])
    except ValueError:
        raise Exception("Failed to parse response JSON")



