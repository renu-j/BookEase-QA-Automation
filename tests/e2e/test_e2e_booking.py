import pytest

from pages.availability_page.availability_page import AvailabilityPage
from pages.room_selection_page.room_selection_page import RoomSelectionPage
from pages.booking_page import BookingPage
from pages.rooms_page import RoomsPage


@pytest.mark.ui
@pytest.mark.e2e
def test_complete_hotel_booking_e2e(driver):

    # STEP 1: Open hotel website
    driver.get("https://automationintesting.online/")

    # STEP 2: Enter valid check-in and check-out dates
    availability = AvailabilityPage(driver)

    availability.enter_check_in("27/09/2026")
    availability.enter_check_out("28/09/2026")

    # STEP 3: Check room availability
    availability.click_check_availability()

    # STEP 4: Verify available rooms
    rooms = RoomsPage(driver)

    room_count = rooms.get_room_count()

    assert room_count > 0, \
        "No available rooms were displayed"

    # STEP 5: Select Single Room
    rooms.click_single_room()

    # STEP 6: Open reservation from Room Selection page
    room_selection = RoomSelectionPage(driver)

    room_selection.click_reserve_now()

    # STEP 7: Enter valid guest details
    booking = BookingPage(driver)

    booking.enter_first_name("Toya")
    booking.enter_last_name("Test")
    booking.enter_email("toya.test@example.com")
    booking.enter_phone("981234578678")

    # STEP 8: Submit the booking
    booking.click_reserve()

    # STEP 9: Verify booking confirmation
    assert booking.is_booking_confirmed(), \
        "Booking confirmation was not displayed"
