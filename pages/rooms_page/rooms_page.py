from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

from pages.rooms_page.rooms_locators import (
    ROOMS_SECTION,
    ROOM_CARDS,
    ROOM_TITLES,
    SINGLE_ROOM_BOOK_NOW,
)


class RoomsPage(BasePage):

    def is_rooms_section_visible(self):
        return self.is_visible(ROOMS_SECTION)

    def get_room_count(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*ROOM_CARDS)
            ) > 0
        )

        return len(
            self.driver.find_elements(*ROOM_CARDS)
        )

    def has_rooms(self):
        return len(
            self.driver.find_elements(*ROOM_CARDS)
        ) > 0

    def get_room_titles(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*ROOM_TITLES)
            ) > 0
        )

        elements = self.driver.find_elements(*ROOM_TITLES)

        return [
            element.text.strip()
            for element in elements
        ]

    def click_single_room(self):
        element = self.wait.until(
            EC.presence_of_element_located(
                SINGLE_ROOM_BOOK_NOW
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )