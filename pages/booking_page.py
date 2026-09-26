from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BookingPage(BasePage):

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

    def enter_first_name(self, name):
        self.enter_text(self.FIRST_NAME, name)

    def enter_last_name(self, name):
        self.enter_text(self.LAST_NAME, name)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_phone(self, phone):
        self.enter_text(self.PHONE, phone)

    def click_reserve(self):
        self.click(self.RESERVE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_validation_messages(self):
        return self.get_text(self.VALIDATION_ALERT)

    def is_booking_confirmed(self):
        return self.is_visible(self.BOOKING_CONFIRMED)