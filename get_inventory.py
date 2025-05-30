# import requests
# import urllib3
# import json
#
# # ✅ Disable warnings for self-signed certificates (used by Cisco sandbox)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
# # ✅ API base details for Cisco SD-WAN sandbox
# BASE_URL = "https://sandbox-sdwan-2.cisco.com"
# USERNAME = "devnetuser"
# PASSWORD = "RG!_Yw919_83"
#
# # ✅ Step 1: Authenticate and get token
# def authenticate():
#     login_url = f"{BASE_URL}/j_security_check"
#     payload = {
#         "j_username": USERNAME,
#         "j_password": PASSWORD
#     }
#
#     session = requests.session()
#     response = session.post(login_url, data=payload, verify=False)
#
#     if response.status_code == 200 and "JSESSIONID" in session.cookies:
#         # Get XSRF token
#         token_url = f"{BASE_URL}/dataservice/client/token"
#         token_response = session.get(token_url, verify=False)
#
#         if token_response.status_code == 200:
#             session.headers["X-XSRF-TOKEN"] = token_response.text
#             print("[+] Authenticated successfully.")
#             return session
#         else:
#             print("[-] Failed to retrieve XSRF token.")
#             exit()
#     else:
#         print("[-] Login failed.")
#         exit()
#
# # ✅ Step 2: Get device inventory
# def get_device_inventory(session):
#     inventory_url = f"{BASE_URL}/dataservice/device"
#     response = session.get(inventory_url, verify=False)
#
#     print(f"[i] Status Code: {response.status_code}")
#     try:
#         json_data = response.json()
#         print(f"[i] JSON Keys: {list(json_data.keys())}")
#     except Exception as e:
#         print("[-] Failed to parse JSON response.")
#         print("Error:", str(e))
#         print("Raw Response:", response.text)
#         return
#
#     if "data" not in json_data:
#         print("[-] 'data' key not in response.")
#         return
#
#     devices = json_data["data"]
#     print(f"[+] Found {len(devices)} devices:")
#     for device in devices:
#         hostname = device.get("host-name", "N/A")
#         device_type = device.get("device-type", "N/A")
#         system_ip = device.get("system-ip", "N/A")
#         uuid = device.get("uuid", "N/A")
#         print(f"- {hostname} ({device_type}) | IP: {system_ip} | UUID: {uuid}")
#
#
# # ✅ Step 3: Run the functions
# if __name__ == "__main__":
#     session = authenticate()
#     get_device_inventory(session)



# 33333333333333333

from auth import authenticate
from api_helper import get_device_inventory

if __name__ == "__main__":
    session = authenticate()
    devices = get_device_inventory(session)

    print(f"[+] Found {len(devices)} devices:")
    for device in devices:
        print(f"- {device['host-name']} ({device['device-type']})")
