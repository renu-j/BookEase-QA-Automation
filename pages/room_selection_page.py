from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RoomDetailsPage(BasePage):

    RESERVE_NOW_BUTTON = (
        By.ID,
        "doReservation"
    )

    def click_reserve_now(self):
        self.click(self.RESERVE_NOW_BUTTON)