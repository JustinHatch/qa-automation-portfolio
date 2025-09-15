import requests
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"
AUTH_ENDPOINT = f"{BASE_URL}/auth"

# Sample credentials from the screenshot
auth_payload = {
    "username": "admin",
    "password": "password123"
}


def test_authentication_success():
    response = requests.post(
        AUTH_ENDPOINT,
        headers={"Content-Type": "application/json"},
        json=auth_payload
    )
    print("Response JSON:", response.json())

    # Status code should be 200
    assert response.status_code == 200

    # Response should contain a token
    json_data = response.json()
    assert "token" in json_data
    assert isinstance(json_data["token"], str)
