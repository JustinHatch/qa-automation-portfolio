import requests
import pytest


def test_get_users_page_2():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    # Status code check
    assert response.status_code == 200

    # Check that 'data' key is in response
    json_data = response.json()
    assert "data" in json_data
    assert len(json_data["data"]) > 0

    # Check that a specific email exists in the results
    emails = [user["email"] for user in json_data["data"]]
    assert "michael.lawson@reqres.in" in emails
