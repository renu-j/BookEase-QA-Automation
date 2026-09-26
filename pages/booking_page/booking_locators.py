from selenium.webdriver.common.by import By


FIRST_NAME = (By.NAME, "firstname")

LAST_NAME = (By.NAME, "lastname")

EMAIL = (By.NAME, "email")

PHONE = (By.NAME, "phone")


RESERVE_BUTTON = (
    By.CSS_SELECTOR,
    "button.btn-primary[type='button']"
)

CANCEL_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Cancel']"
)

VALIDATION_ALERT = (
    By.CSS_SELECTOR,
    "div.alert.alert-danger[role='alert']"
)

BOOKING_CONFIRMED = (
    By.XPATH,
    "//h2[normalize-space()='Booking Confirmed']"
)