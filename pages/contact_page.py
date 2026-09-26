from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    SUBJECT = (By.ID, "subject")
    MESSAGE = (By.ID, "description")

    SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        "#contact button.btn.btn-primary[type='button']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h3[contains(normalize-space(), 'Thanks for getting in touch')]"
    )

    VALIDATION_ALERT = (
        By.CSS_SELECTOR,
        "#contact div.alert.alert-danger"
    )

    def enter_name(self, name):
        self.enter_text(self.NAME, name)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_phone(self, phone):
        self.enter_text(self.PHONE, phone)

    def enter_subject(self, subject):
        self.enter_text(self.SUBJECT, subject)

    def enter_message(self, message):
        self.enter_text(self.MESSAGE, message)

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_validation_messages(self):
        return self.get_text(self.VALIDATION_ALERT)