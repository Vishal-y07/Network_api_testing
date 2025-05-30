import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

def authenticate():
    session = requests.session()
    auth_url = f"{BASE_URL}/j_security_check"
    payload = {
        "j_username": USERNAME,
        "j_password": PASSWORD
    }

    response = session.post(auth_url, data=payload, verify=False)

    if response.status_code == 200 and "JSESSIONID" in session.cookies:
        print("[+] Authenticated successfully.")
        headers = {"Content-Type": "application/json"}
        return session, headers  # ✅ Now returns both

    else:
        raise Exception("[-] Authentication failed.")

def get_auth_token(session):
    """
    Fetch X-XSRF-TOKEN after successful authentication.
    """
    token_url = f"{BASE_URL}/dataservice/client/token"
    response = session.get(token_url, verify=False)

    if response.status_code == 200:
        token = response.text
        return token
    else:
        raise Exception("[-] Failed to fetch X-XSRF-TOKEN.")