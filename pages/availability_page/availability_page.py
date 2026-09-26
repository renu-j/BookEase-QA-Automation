from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

from pages.availability_page.availability_locators import (
    CHECK_IN,
    CHECK_OUT,
    CHECK_AVAILABILITY_BUTTON,
)


class AvailabilityPage(BasePage):

    def enter_check_in(self, date):
        element = self.wait.until(
            EC.element_to_be_clickable(CHECK_IN)
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
            EC.element_to_be_clickable(CHECK_OUT)
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
            EC.element_to_be_clickable(CHECK_IN)
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
            EC.element_to_be_clickable(CHECK_OUT)
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
        self.click(CHECK_AVAILABILITY_BUTTON)

    def is_availability_button_visible(self):
        return self.is_visible(CHECK_AVAILABILITY_BUTTON)


    def get_check_in_value(self):
        return self.driver.find_element(*CHECK_IN).get_attribute("value")


    def get_check_out_value(self):
       return self.driver.find_element(*CHECK_OUT).get_attribute("value")