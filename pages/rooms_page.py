from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class RoomsPage(BasePage):

    ROOMS_SECTION = (By.ID, "rooms")

    ROOM_CARDS = (
        By.CSS_SELECTOR,
        "#rooms .card"
    )

    ROOM_TITLES = (
        By.CSS_SELECTOR,
        "#rooms .card-title"
    )

    BOOK_NOW_BUTTONS = (
        By.XPATH,
        "//section[@id='rooms']//a[contains(normalize-space(), 'Book now')]"
    )

    def is_rooms_section_visible(self):
        return self.is_visible(self.ROOMS_SECTION)

    def get_room_count(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.ROOM_CARDS)
            ) > 0
        )

        return len(
            self.driver.find_elements(*self.ROOM_CARDS)
        )

    def has_rooms(self):
        return len(
            self.driver.find_elements(*self.ROOM_CARDS)
        ) > 0

    def get_room_titles(self):
        self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.ROOM_TITLES)
            ) > 0
        )

        elements = self.driver.find_elements(*self.ROOM_TITLES)

        return [element.text.strip() for element in elements]

    def get_book_now_button_count(self):
        return len(
            self.driver.find_elements(*self.BOOK_NOW_BUTTONS)
        )

    # E2E: Select the Single room
    def click_single_room(self):
        single_room_book_now = (
            By.XPATH,
            "//section[@id='rooms']"
            "//div[contains(@class,'room-card')][.//*[normalize-space()='Single']]"
            "//a[contains(normalize-space(), 'Book now')]"
        )

        element = self.wait.until(
            EC.presence_of_element_located(single_room_book_now)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

