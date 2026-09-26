import pytest

from pages.booking_page import BookingPage


# ============================================================
# BK-01: Phone number below minimum length
# Type: Negative + Boundary
# Rule discovered from application:
# Phone length must be between 11 and 21 characters.
#
# 10 digits → INVALID
# Expected: Validation message and no booking confirmation
# ============================================================

@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.boundary
def test_booking_with_phone_below_minimum(driver):
    """
    Verify that a 10-digit phone number is rejected.

    Boundary condition:
    Minimum accepted phone length = 11
    Test value = 10 digits
    """

    driver.get(
        "https://automationintesting.online/reservation/1"
        "?checkin=2026-10-01&checkout=2026-10-02"
    )

    booking_page = BookingPage(driver)

    # Open booking form
    booking_page.click_reserve()

    # Enter valid customer information
    booking_page.enter_first_name("Renu")
    booking_page.enter_last_name("Twinkle")
    booking_page.enter_email("renu.twinkle@example.com")

    # 10 digits → below minimum boundary
    booking_page.enter_phone("9878787927")

    # Submit booking
    booking_page.click_reserve()

    # Capture validation result
    driver.save_screenshot(
        "screenshots/bk01_phone_below_minimum.png"
    )

    # Verify phone validation message
    messages = booking_page.get_validation_messages()

    assert "size must be between 11 and 21" in messages

    # Booking must not be confirmed
    assert not booking_page.is_booking_confirmation_present(), \
        "Booking was confirmed with an invalid phone number"


# ============================================================
# BK-02: Phone number at minimum valid boundary
# Type: Positive + Boundary
#
# 11 digits → VALID
# Expected: Booking Confirmed
# ============================================================

@pytest.mark.ui
@pytest.mark.boundary
def test_booking_with_minimum_valid_phone(driver):
    """
    Verify that a booking succeeds with exactly 11 digits.

    Boundary condition:
    Minimum accepted phone length = 11
    Test value = exactly 11 digits
    """

    driver.get(
        "https://automationintesting.online/reservation/1"
        "?checkin=2026-10-03&checkout=2026-10-04"
    )

    booking_page = BookingPage(driver)

    # Open booking form
    booking_page.click_reserve()

    # Enter valid customer information
    booking_page.enter_first_name("Renu")
    booking_page.enter_last_name("Twinkle")
    booking_page.enter_email("renu.twinkle@example.com")

    # Exactly 11 digits → minimum valid boundary
    booking_page.enter_phone("98787879270")

    # Submit booking
    booking_page.click_reserve()

    # Capture successful booking
    driver.save_screenshot(
        "screenshots/bk02_minimum_valid_phone.png"
    )

    # Verify actual business result
    assert booking_page.is_booking_confirmed(), \
        "Booking confirmation page was not displayed"


# ============================================================
# BK-03: Phone number at maximum valid boundary
# Type: Positive + Boundary
#
# 21 digits → VALID
# Expected: Booking Confirmed
# ============================================================

@pytest.mark.ui
@pytest.mark.boundary
def test_booking_with_maximum_valid_phone(driver):
    """
    Verify that a booking succeeds with exactly 21 digits.

    Boundary condition:
    Maximum accepted phone length = 21
    Test value = exactly 21 digits
    """

    driver.get(
        "https://automationintesting.online/reservation/1"
        "?checkin=2026-10-05&checkout=2026-10-06"
    )

    booking_page = BookingPage(driver)

    # Open booking form
    booking_page.click_reserve()

    # Enter valid customer information
    booking_page.enter_first_name("Renu")
    booking_page.enter_last_name("Twinkle")
    booking_page.enter_email("renu.twinkle@example.com")

    # Exactly 21 digits → maximum valid boundary
    booking_page.enter_phone(
        "123456789012345678901"
    )

    # Submit booking
    booking_page.click_reserve()

    # Capture successful booking
    driver.save_screenshot(
        "screenshots/bk03_maximum_valid_phone.png"
    )

    # Verify actual business result
    assert booking_page.is_booking_confirmed(), \
        "Booking confirmation page was not displayed"


# ============================================================
# BK-04: Phone number above maximum length
# Type: Negative + Boundary
#
# 22 digits → INVALID
# Expected: Validation message and no booking confirmation
# ============================================================

@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.boundary
def test_booking_with_phone_above_maximum(driver):
    """
    Verify that a 22-digit phone number is rejected.

    Boundary condition:
    Maximum accepted phone length = 21
    Test value = 22 digits
    """

    driver.get(
        "https://automationintesting.online/reservation/1"
        "?checkin=2026-10-07&checkout=2026-10-08"
    )

    booking_page = BookingPage(driver)

    # Open booking form
    booking_page.click_reserve()

    # Enter valid customer information
    booking_page.enter_first_name("Renu")
    booking_page.enter_last_name("Twinkle")
    booking_page.enter_email("renu.twinkle@example.com")

    # 22 digits → above maximum boundary
    booking_page.enter_phone(
        "1234567890123456789012"
    )

    # Submit booking
    booking_page.click_reserve()

    # Capture validation result
    driver.save_screenshot(
        "screenshots/bk04_phone_above_maximum.png"
    )

    # Verify phone validation message
    messages = booking_page.get_validation_messages()

    assert "size must be between 11 and 21" in messages

    # Booking must not be confirmed
    assert not booking_page.is_booking_confirmation_present(), \
        "Booking was confirmed with an invalid phone number"