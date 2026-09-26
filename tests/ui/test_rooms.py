import pytest

from pages.rooms_page import RoomsPage


BASE_URL = "https://automationintesting.online/"


@pytest.mark.ui
def test_rooms_section_is_visible(driver):
    driver.get(BASE_URL)

    rooms_page = RoomsPage(driver)

    assert rooms_page.is_rooms_section_visible(), \
        "Rooms section is not visible"


@pytest.mark.ui
def test_rooms_are_displayed(driver):
    driver.get(BASE_URL)

    rooms_page = RoomsPage(driver)

    room_count = rooms_page.get_room_count()

    assert room_count > 0, \
        "No rooms are displayed"


@pytest.mark.ui
def test_room_names_are_displayed(driver):
    driver.get(BASE_URL)

    rooms_page = RoomsPage(driver)

    room_titles = rooms_page.get_room_titles()

    assert "Single" in room_titles
    assert "Double" in room_titles
    assert "Suite" in room_titles

