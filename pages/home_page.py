from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    ROOMS_LINK = (By.CSS_SELECTOR, 'a[href="#rooms"]')
    ROOMS_SECTION = (By.ID, "rooms")

    NAVIGATION = (By.CSS_SELECTOR, "nav")

    HOTEL_HEADING = (
        By.XPATH,
        "//h1[contains(normalize-space(), 'Welcome to Shady Meadows B&B')]"
    )

    def open(self, url):
        self.driver.get(url)

    def click_rooms(self):
        self.click(self.ROOMS_LINK)

    def is_rooms_section_visible(self):
        return self.is_visible(self.ROOMS_SECTION)

    def is_navigation_visible(self):
        return self.is_visible(self.NAVIGATION)

    def is_hotel_heading_visible(self):
        return self.is_visible(self.HOTEL_HEADING)