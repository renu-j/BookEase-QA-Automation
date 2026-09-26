import pytest

from pages.home_page import HomePage
from pages.availability_page.availability_page import AvailabilityPage
from pages.rooms_page import RoomsPage


# ============================================================
# AV-01: Valid check-in and check-out dates
# Positive / Functional
# ============================================================

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


# ============================================================
# AV-02: Valid multi-night stay
# Positive / Functional
# ============================================================

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


# ============================================================
# AV-03: Check-out before check-in
# Negative / Validation
# ============================================================

@pytest.mark.ui
def test_checkout_before_checkin(driver):

    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("30/09/2026")
    availability_page.enter_check_out("24/09/2026")

    availability_page.click_check_availability()

    driver.save_screenshot(
        "reports/av03_result.png"
    )

    assert availability_page.is_availability_button_visible(), \
        "Application proceeded from the availability form for an invalid date range"


# ============================================================
# AV-04: Same check-in and check-out date
# Boundary / Validation
# ============================================================

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


# ============================================================
# AV-05: Clear check-in date
# Negative / State
# ============================================================

@pytest.mark.ui
def test_clear_checkin_date(driver):

    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("24/09/2026")

    availability_page.clear_check_in()

    checkin_value = availability_page.get_check_in_value()

    assert checkin_value == "", \
        "Check-in date was not cleared successfully"


# ============================================================
# AV-06: Clear check-out date
# Negative / State
# ============================================================

@pytest.mark.ui
def test_clear_checkout_date(driver):

    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_out("25/09/2026")

    availability_page.clear_check_out()

    checkout_value = availability_page.get_check_out_value()

    assert checkout_value == "", \
        "Check-out date was not cleared successfully"


# ============================================================
# AV-07: Historical dates
# Negative / Functional
# ============================================================

@pytest.mark.ui
@pytest.mark.negative
def test_availability_with_historical_dates(driver):

    home_page = HomePage(driver)
    availability_page = AvailabilityPage(driver)

    home_page.open("https://automationintesting.online/")

    availability_page.enter_check_in("25/09/0001")
    availability_page.enter_check_out("16/09/0002")

    availability_page.click_check_availability()