import requests
import pytest

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_API_URL = "https://automationintesting.online/api"


@pytest.mark.api
def test_login():
    """Verify valid user can log in successfully."""

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


@pytest.mark.api
def test_login_invalid_password():
    """Verify login fails with an incorrect password."""

    response = requests.post(
        f"{BASE_API_URL}/auth/login",
        json={
            "username": "admin",
            "password": "wrongpassword"
        },
        verify=False
    )

    assert response.status_code == 401


@pytest.mark.api
def test_login_invalid_username():
    """Verify login fails with an incorrect username."""

    response = requests.post(
        f"{BASE_API_URL}/auth/login",
        json={
            "username": "wronguser",
            "password": "password"
        },
        verify=False
    )

    assert response.status_code == 401