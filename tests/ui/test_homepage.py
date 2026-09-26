import pytest
from pages.home_page import HomePage


@pytest.mark.ui
def test_home_page_loads(driver):
    home_page = HomePage(driver)

    home_page.open("https://automationintesting.online/")

    assert "Restful-booker-platform demo" in driver.title


@pytest.mark.ui
def test_navigation_is_visible(driver):
    home_page = HomePage(driver)

    home_page.open("https://automationintesting.online/")

    assert home_page.is_navigation_visible()

@pytest.mark.ui
def test_hotel_heading_is_visible(driver):
    home_page = HomePage(driver)

    home_page.open("https://automationintesting.online/")

    assert home_page.is_hotel_heading_visible()