import pytest
from pages.home_page import HomePage
from pages.rooms_page import RoomsPage


@pytest.mark.ui
def test_rooms_section_is_visible(driver):
    home_page = HomePage(driver)
    rooms_page = RoomsPage(driver)

    home_page.open("https://automationintesting.online/")

    assert rooms_page.is_rooms_section_visible()

@pytest.mark.ui
def test_rooms_are_displayed(driver):
    home_page = HomePage(driver)
    rooms_page = RoomsPage(driver)

    home_page.open("https://automationintesting.online/")

    room_count = rooms_page.get_room_count()

    assert room_count > 0, "No rooms are displayed"

@pytest.mark.ui
def test_room_names_are_displayed(driver):
    home_page = HomePage(driver)
    rooms_page = RoomsPage(driver)

    home_page.open("https://automationintesting.online/")

    room_titles = rooms_page.get_room_titles()

    assert "Single" in room_titles
    assert "Double" in room_titles
    assert "Suite" in room_titles