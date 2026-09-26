from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class AvailabilityPage(BasePage):

    CHECK_IN = (
        By.XPATH,
        "//label[@for='checkin']/following-sibling::div//input"
    )

    CHECK_OUT = (
        By.XPATH,
        "//label[@for='checkout']/following-sibling::div//input"
    )

    CHECK_AVAILABILITY_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Check Availability']"
    )

    def enter_check_in(self, date):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CHECK_IN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(date)

    def enter_check_out(self, date):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CHECK_OUT)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(date)

    def clear_check_in(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CHECK_IN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)

    def clear_check_out(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CHECK_OUT)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)



    def click_check_availability(self):
        self.click(self.CHECK_AVAILABILITY_BUTTON)

    def is_availability_button_visible(self):
        return self.is_visible(self.CHECK_AVAILABILITY_BUTTON)