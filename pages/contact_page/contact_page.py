from pages.base_page import BasePage

from pages.contact_page.contact_locators import (
    NAME,
    EMAIL,
    PHONE,
    SUBJECT,
    MESSAGE,
    SUBMIT_BUTTON,
    SUCCESS_MESSAGE,
    VALIDATION_ALERT,
)


class ContactPage(BasePage):

    def enter_name(self, name):
        self.enter_text(NAME, name)

    def enter_email(self, email):
        self.enter_text(EMAIL, email)

    def enter_phone(self, phone):
        self.enter_text(PHONE, phone)

    def enter_subject(self, subject):
        self.enter_text(SUBJECT, subject)

    def enter_message(self, message):
        self.enter_text(MESSAGE, message)

    def click_submit(self):
        self.click(SUBMIT_BUTTON)

    def get_success_message(self):
        return self.get_text(SUCCESS_MESSAGE)

    def get_validation_messages(self):
        return self.get_text(VALIDATION_ALERT)