from pages.base_page import BasePage

from pages.room_selection_page.room_selection_locators import (
    RESERVE_NOW_BUTTON,
)


class RoomSelectionPage(BasePage):

    def click_reserve_now(self):
        self.click(RESERVE_NOW_BUTTON)