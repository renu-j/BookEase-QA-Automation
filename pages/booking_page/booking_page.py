
from pages.base_page import BasePage

from pages.booking_page.booking_locators import (
    FIRST_NAME,
    LAST_NAME,
    EMAIL,
    PHONE,
    RESERVE_BUTTON,
    CANCEL_BUTTON,
    VALIDATION_ALERT,
    BOOKING_CONFIRMED,
)


class BookingPage(BasePage):

    def enter_first_name(self, name):
        self.enter_text(FIRST_NAME, name)

    def enter_last_name(self, name):
        self.enter_text(LAST_NAME, name)

    def enter_email(self, email):
        self.enter_text(EMAIL, email)

    def enter_phone(self, phone):
        self.enter_text(PHONE, phone)

    def click_reserve(self):
        self.click(RESERVE_BUTTON)

    def click_cancel(self):
        self.click(CANCEL_BUTTON)

    def get_validation_messages(self):
        return self.get_text(VALIDATION_ALERT)

    def is_booking_confirmed(self):
        return self.is_visible(BOOKING_CONFIRMED)

    def is_booking_confirmation_present(self):
        return self.is_element_present(BOOKING_CONFIRMED)

