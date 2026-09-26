import requests
import pytest


BASE_API_URL = "https://automationintesting.online/api"


@pytest.mark.api
def test_get_bookings():

    # Create a session so cookies are preserved
    session = requests.Session()

    # Step 1: Login
    login_response = session.post(
        f"{BASE_API_URL}/auth/login",
        json={
            "username": "admin",
            "password": "password"
        },
        verify=False
    )

    assert login_response.status_code == 200

    token = login_response.json()["token"]

    # Step 2: Explicitly set the authentication cookie
    session.cookies.set("token", token)

    # Step 3: Get bookings for Room ID 1
    response = session.get(
        f"{BASE_API_URL}/booking/?roomid=1",
        verify=False
    )

    # Step 4: Validate response
    assert response.status_code == 200

    data = response.json()

    assert "bookings" in data