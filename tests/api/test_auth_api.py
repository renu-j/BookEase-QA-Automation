
import requests
import pytest

BASE_API_URL = "https://automationintesting.online/api"


@pytest.mark.api
def test_login():
    response = requests.post(
        f"{BASE_API_URL}/auth/login",
        json={
            "username": "admin",
            "password": "password"
        },
        verify=False
    )

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert data["token"]
