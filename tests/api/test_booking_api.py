
import requests
import pytest


import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_API_URL = "https://automationintesting.online/api"

#helper function
def get_authenticated_session():
    """Login and return an authenticated session."""
    session = requests.Session()

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

    session.cookies.set("token", token)

    return session


@pytest.mark.api
def test_get_bookings():
    """Verify authenticated user can retrieve bookings."""

    session = get_authenticated_session()

    response = session.get(
        f"{BASE_API_URL}/booking/?roomid=1",
        verify=False
    )

    assert response.status_code == 200

    data = response.json()

    assert "bookings" in data
    assert isinstance(data["bookings"], list)


@pytest.mark.api
def test_create_booking():
    """Verify authenticated user can create a booking."""

    session = get_authenticated_session()

    booking_data = {
        "roomid": 1,
        "firstname": "API",
        "lastname": "Automation",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2027-06-01",
            "checkout": "2027-06-05"
        }
    }

    response = session.post(
        f"{BASE_API_URL}/booking",
        json=booking_data,
        verify=False
    )

    assert response.status_code == 201

    data = response.json()

    # API returns the newly created booking ID
    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)



@pytest.mark.api
def test_delete_booking():
    """Verify authenticated user can delete a booking."""

    session = get_authenticated_session()

    # Step 1: Create a booking
    booking_data = {
        "roomid": 1,
        "firstname": "Delete",
        "lastname": "Test",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2027-08-01",
            "checkout": "2027-08-05"
        }
    }

    create_response = session.post(
        f"{BASE_API_URL}/booking",
        json=booking_data,
        verify=False
    )

    assert create_response.status_code == 201

    booking_id = create_response.json()["bookingid"]

    # Step 2: Delete the booking
    delete_response = session.delete(
        f"{BASE_API_URL}/booking/{booking_id}",
        verify=False
    )

    # Step 3: Validate deletion
    assert delete_response.status_code == 202
