
import pytest

from pages.contact_page import ContactPage


# CT-01: Verify successful submission of the Contact Form
# Type: Positive | UI Functional
# Expected Result: Form is submitted successfully and the confirmation
# message "Thanks for getting in touch" is displayed.
@pytest.mark.ui
def test_valid_contact_submission(driver):
    driver.get("https://automationintesting.online/#contact")

    contact_page = ContactPage(driver)

    # Enter valid data in all mandatory fields.
    contact_page.enter_name("Renu")
    contact_page.enter_email("renu.twinkle@example.com")
    contact_page.enter_phone("98688097130")
    contact_page.enter_subject("Traveling")
    contact_page.enter_message(
        "I would like to know more about staying at your hotel."
    )

    # Submit the completed form.
    contact_page.click_submit()

    # Verify that the application displays the successful submission message.
    success_message = contact_page.get_success_message()

    assert "Thanks for getting in touch" in success_message


# CT-02: Verify validation for an empty Contact Form
# Type: Negative | UI Functional | Validation
# Expected Result: Submission is prevented and validation messages are
# displayed for all mandatory fields.
@pytest.mark.ui
@pytest.mark.negative
def test_empty_contact_form_validation(driver):
    driver.get("https://automationintesting.online/#contact")

    contact_page = ContactPage(driver)

    # Submit the form without entering any information.
    contact_page.click_submit()

    # Capture the validation messages displayed by the application.
    messages = contact_page.get_validation_messages()

    # Verify that each mandatory field is validated.
    assert "Name may not be blank" in messages
    assert "Email may not be blank" in messages
    assert "Phone may not be blank" in messages
    assert "Subject may not be blank" in messages
    assert "Message may not be blank" in messages


# CT-03: Verify phone number minimum-length validation
# Type: Negative | UI Functional | Boundary
# Expected Result: A phone number containing fewer than 11 characters
# is rejected with the appropriate validation message.
@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.boundary
def test_phone_below_minimum_length(driver):
    driver.get("https://automationintesting.online/#contact")

    contact_page = ContactPage(driver)

    # Enter valid data in all fields except Phone.
    # 10 characters are intentionally provided to test the lower boundary.
    contact_page.enter_name("Renu")
    contact_page.enter_email("renu.twinkle@example.com")
    contact_page.enter_phone("9868809713")
    contact_page.enter_subject("Traveling")
    contact_page.enter_message(
        "I would like to know more about staying at your hotel."
    )

    # Submit the form with an invalid phone number.
    contact_page.click_submit()

    # Verify the phone-length validation message.
    messages = contact_page.get_validation_messages()

    assert "Phone must be between 11 and 21 characters." in messages


# CT-04: Verify message minimum-length validation
# Type: Negative | UI Functional | Boundary
# Expected Result: A message containing fewer than 20 characters
# is rejected with the appropriate validation message.
@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.boundary
def test_message_below_minimum_length(driver):
    driver.get("https://automationintesting.online/#contact")

    contact_page = ContactPage(driver)

    # Enter valid data in all fields except Message.
    # A message shorter than 20 characters is intentionally provided
    # to test the lower boundary.
    contact_page.enter_name("Renu")
    contact_page.enter_email("renu.twinkle@example.com")
    contact_page.enter_phone("98688097130")
    contact_page.enter_subject("Traveling")
    contact_page.enter_message("Short message")

    # Submit the form with an invalid message length.
    contact_page.click_submit()

    # Verify the message-length validation.
    messages = contact_page.get_validation_messages()

    assert "Message must be between 20 and 2000 characters." in messages


# CT-08: Verify valid minimum boundary values
# Type: Positive | UI Functional | Boundary
# Expected Result: The form is successfully submitted when Phone
# contains exactly 11 characters and Message contains exactly 20 characters.
@pytest.mark.ui
@pytest.mark.boundary
def test_valid_minimum_boundary_values(driver):
    driver.get("https://automationintesting.online/#contact")

    contact_page = ContactPage(driver)

    # Enter valid data using the minimum allowed boundary values.
    contact_page.enter_name("Renu")
    contact_page.enter_email("renu.twinkle@example.com")

    # Exactly 11 characters — minimum allowed phone length.
    contact_page.enter_phone("98688097130")

    contact_page.enter_subject("Traveling")

    # Exactly 20 characters — minimum allowed message length.
    contact_page.enter_message("12345678901234567890")

    # Submit the form.
    contact_page.click_submit()

    # Verify that the application accepts the minimum valid values.
    success_message = contact_page.get_success_message()

    print("\n===== ACTUAL APPLICATION RESPONSE =====")
    print("Success message:", success_message)
    print("=======================================")

    assert "Thanks for getting in touch" in success_message

    assert "Thanks for getting in touch" in success_message


