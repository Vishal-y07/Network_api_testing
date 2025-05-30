import pytest
from auth import authenticate, get_auth_token
from api_helper import BASE_URL

def test_token_retrieval():
    session, _ = authenticate()
    token = get_auth_token(session)

    assert token and len(token) > 10, "Invalid or empty token"
    print(f"[+] Retrieved token: {token[:10]}...")

def test_token_access_protected_api():
    session, _ = authenticate()
    token = get_auth_token(session)

    headers = {
        "Content-Type": "application/json",
        "X-XSRF-TOKEN": token
    }

    response = session.get(f"{BASE_URL}/dataservice/device", headers=headers, verify=False)
    assert response.status_code == 200, "Token-authenticated request failed"

@pytest.mark.xfail(reason="Sandbox may allow access even without token")
def test_access_without_token_header():
    session, _ = authenticate()
    response = session.get(f"{BASE_URL}/dataservice/device", verify=False)

    assert response.status_code == 403, "Expected 403 without token"
