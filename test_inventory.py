import pytest
import time
from jsonschema import validate
from auth import authenticate
from api_helper import get_device_inventory

# ✅ JSON schema to validate each device
device_schema = {
    "type": "object",
    "properties": {
        "deviceId": {"type": "string"},
        "host-name": {"type": "string"},
        "device-type": {"type": "string"},
        "reachability": {"type": "string"}
    },
    "required": ["deviceId", "host-name", "device-type", "reachability"]
}

# ✅ Pytest fixture for authenticated session
@pytest.fixture
def api_session():
    """Provides authenticated session and headers."""
    session, headers = authenticate()
    return session, headers

# ✅ Test basic inventory retrieval and structure
def test_inventory_structure(api_session):
    session, headers = api_session
    inventory = get_device_inventory(session, headers)

    assert isinstance(inventory, list), "Inventory should be a list"
    assert len(inventory) > 0, "Inventory is empty"

# ✅ Test for presence of required fields
def test_inventory_fields(api_session):
    session, headers = api_session
    inventory = get_device_inventory(session, headers)

    for device in inventory:
        assert "deviceId" in device, "Missing deviceId"
        assert "host-name" in device, "Missing host-name"
        assert "reachability" in device, "Missing reachability"

# ✅ Test known device types
def test_known_device_types(api_session):
    session, headers = api_session
    inventory = get_device_inventory(session, headers)

    valid_types = {"vedge", "vsmart", "vbond", "vmanage"}

    for device in inventory:
        assert device["device-type"] in valid_types, f"Unknown device type: {device['device-type']}"

# ✅ Test response time under threshold
def test_inventory_response_time(api_session):
    session, headers = api_session

    start_time = time.time()
    _ = get_device_inventory(session, headers)
    response_time = time.time() - start_time

    assert response_time < 2, f"API took too long to respond: {response_time:.2f}s"

# ✅ Test schema validation (already done earlier)
def test_inventory_schema(api_session):
    session, headers = api_session
    inventory = get_device_inventory(session, headers)

    for device in inventory:
        validate(instance=device, schema=device_schema)

# Define valid types we want to verify against
@pytest.mark.parametrize("expected_type", ["vedge", "vsmart", "vbond", "vmanage"])
def test_device_type_parametrized(api_session, expected_type):
    session, headers = api_session
    inventory = get_device_inventory(session, headers)

    # At least one device should match each expected type
    matches = [dev for dev in inventory if dev.get("device-type") == expected_type]
    assert matches, f"No devices found with device-type: {expected_type}"