import pytest

from pages.home_page import HomePage
from pages.availability_page import AvailabilityPage
from pages.rooms_page import RoomsPage


# AV-01: Verify that available rooms are displayed for valid check-in and check-out dates.
# Positive / Functional
# In short: Valid dates → rooms available

@pytest.mark.ui
def test_availability_with_valid_dates(driver):
    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)
    rooms_page = RoomsPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("24/09/2026")
    availability_page.enter_check_out("25/09/2026")
    availability_page.click_check_availability()

    room_count = rooms_page.get_room_count()

    assert room_count > 0, \
        "No rooms are available for the selected dates"


# AV-02: Verify that availability search displays the rooms section for a valid multi-night stay.
# Positive / Functional
# In short: Valid multi-night search → results

@pytest.mark.ui
def test_availability_with_multi_night_stay(driver):
    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)
    rooms_page = RoomsPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("24/09/2026")
    availability_page.enter_check_out("30/09/2026")

    availability_page.click_check_availability()

    assert rooms_page.is_rooms_section_visible(), \
        "Rooms section is not displayed after availability search"


# AV-03: Verify application behavior when check-out date is before check-in date.
# Negative / Validation
# In short: Check-out before check-in

@pytest.mark.ui
def test_checkout_before_checkin(driver):
    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("30/09/2026")
    availability_page.enter_check_out("24/09/2026")

    availability_page.click_check_availability()

    driver.save_screenshot("reports/av03_result.png")

    assert availability_page.is_availability_button_visible(), \
        "Application proceeded from the availability form for an invalid date range"


# AV-04: Verify application behavior when check-in and check-out dates are the same.
# Boundary / Validation
# In short: Check-in = check-out

@pytest.mark.ui
def test_same_checkin_checkout_date(driver):
    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)
    rooms_page = RoomsPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("24/09/2026")
    availability_page.enter_check_out("24/09/2026")

    availability_page.click_check_availability()

    assert rooms_page.is_rooms_section_visible(), \
        "Rooms section is not displayed when check-in and check-out dates are the same"


# AV-05: Verify that the check-in date can be cleared.
# Negative / State
# In short: Clear Check-in → field becomes empty

@pytest.mark.ui
def test_clear_checkin_date(driver):
    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("24/09/2026")

    availability_page.clear_check_in()

    checkin_value = driver.find_element(
        *availability_page.CHECK_IN
    ).get_attribute("value")

    assert checkin_value == "", \
        "Check-in date was not cleared successfully"


# AV-06: Verify that the check-out date can be cleared.
# Negative / State
# In short: Clear Check-out → field becomes empty

@pytest.mark.ui
def test_clear_checkout_date(driver):
    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_out("25/09/2026")

    availability_page.clear_check_out()

    checkout_value = driver.find_element(
        *availability_page.CHECK_OUT
    ).get_attribute("value")

    assert checkout_value == "", \
        "Check-out date was not cleared successfully"


#Tests whether the Availability feature accepts
# extremely old historical check-in and check-out dates and displays available rooms.
#CT-AV-07 — Negative UI Functional Test: Historical Date Validation

@pytest.mark.ui
@pytest.mark.negative
def test_availability_with_historical_dates(driver):
    # Test historical dates that were observed to be accepted by the application.
    driver.get("https://automationintesting.online/#availability")

    availability_page = AvailabilityPage(driver)

    # Enter historical check-in date: 25/09/0001
    availability_page.enter_check_in("25/09/0001")

    # Enter historical check-out date: 16/09/0002
    availability_page.enter_check_out("16/09/0002")

    # Submit the availability search.
    availability_page.click_check_availability()