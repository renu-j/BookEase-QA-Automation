from pages.base_page import BasePage

from pages.home_page.home_locators import (
    ROOMS_LINK,
    ROOMS_SECTION,
    NAVIGATION,
    HOTEL_HEADING,
)


class HomePage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def click_rooms(self):
        self.click(ROOMS_LINK)

    def is_rooms_section_visible(self):
        return self.is_visible(ROOMS_SECTION)

    def is_navigation_visible(self):
        return self.is_visible(NAVIGATION)

    def is_hotel_heading_visible(self):
        return self.is_visible(HOTEL_HEADING)