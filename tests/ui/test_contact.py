import pytest

from pages.contact_page.contact_page import ContactPage


# ============================================================
# CT-01: Valid Contact Form Submission
# Type: Positive / Functional
#
# Expected:
# Valid contact information is accepted and the application
# displays the success message.
# ============================================================

@pytest.mark.ui
def test_valid_contact_submission(driver):

    driver.get(
        "https://automationintesting.online/#contact"
    )

    contact_page = ContactPage(driver)

    contact_page.enter_name("Renu")
    contact_page.enter_email(
        "renu.twinkle@example.com"
    )
    contact_page.enter_phone("98688097130")
    contact_page.enter_subject("Traveling")
    contact_page.enter_message(
        "I would like to know more about staying at your hotel."
    )

    contact_page.click_submit()

    success_message = contact_page.get_success_message()

    assert "Thanks for getting in touch" in success_message


# ============================================================
# CT-02: Empty Contact Form
# Type: Negative / Validation
#
# Expected:
# All mandatory fields display validation messages.
# ============================================================

@pytest.mark.ui
@pytest.mark.negative
def test_empty_contact_form_validation(driver):

    driver.get(
        "https://automationintesting.online/#contact"
    )

    contact_page = ContactPage(driver)

    contact_page.click_submit()

    messages = contact_page.get_validation_messages()

    assert "Name may not be blank" in messages
    assert "Email may not be blank" in messages
    assert "Phone may not be blank" in messages
    assert "Subject may not be blank" in messages
    assert "Message may not be blank" in messages


# ============================================================
# CT-03: Phone Below Minimum Length
# Type: Negative / Boundary
#
# Rule:
# Phone must contain between 11 and 21 characters.
#
# Test:
# 10 characters → INVALID
# ============================================================

@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.boundary
def test_phone_below_minimum_length(driver):

    driver.get(
        "https://automationintesting.online/#contact"
    )

    contact_page = ContactPage(driver)

    contact_page.enter_name("Renu")
    contact_page.enter_email(
        "renu.twinkle@example.com"
    )

    # 10 characters → below minimum
    contact_page.enter_phone("9868809713")

    contact_page.enter_subject("Traveling")
    contact_page.enter_message(
        "I would like to know more about staying at your hotel."
    )

    contact_page.click_submit()

    messages = contact_page.get_validation_messages()

    assert "Phone must be between 11 and 21 characters." in messages


# ============================================================
# CT-04: Message Below Minimum Length
# Type: Negative / Boundary
#
# Rule:
# Message must contain between 20 and 2000 characters.
#
# Test:
# Less than 20 characters → INVALID
# ============================================================

@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.boundary
def test_message_below_minimum_length(driver):

    driver.get(
        "https://automationintesting.online/#contact"
    )

    contact_page = ContactPage(driver)

    contact_page.enter_name("Renu")
    contact_page.enter_email(
        "renu.twinkle@example.com"
    )
    contact_page.enter_phone("98688097130")
    contact_page.enter_subject("Traveling")

    # Less than 20 characters → below minimum
    contact_page.enter_message("Short message")

    contact_page.click_submit()

    messages = contact_page.get_validation_messages()

    assert "Message must be between 20 and 2000 characters." in messages


# ============================================================
# CT-05: Minimum Valid Boundary Values
# Type: Positive / Boundary
#
# Phone:
# Exactly 11 characters → VALID
#
# Message:
# Exactly 20 characters → VALID
#
# Expected:
# Contact form is successfully submitted.
# ============================================================

@pytest.mark.ui
@pytest.mark.boundary
def test_valid_minimum_boundary_values(driver):

    driver.get(
        "https://automationintesting.online/#contact"
    )

    contact_page = ContactPage(driver)

    contact_page.enter_name("Renu")
    contact_page.enter_email(
        "renu.twinkle@example.com"
    )

    # Exactly 11 characters → minimum valid phone
    contact_page.enter_phone("98688097130")

    contact_page.enter_subject("Traveling")

    # Exactly 20 characters → minimum valid message
    contact_page.enter_message(
        "12345678901234567890"
    )

    contact_page.click_submit()

    success_message = contact_page.get_success_message()

    assert "Thanks for getting in touch" in success_message