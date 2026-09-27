import pytest

from pages.home_page.home_page import HomePage


# ============================================================
# HM-01: Verify Home Page loads successfully
# Type: Positive / Smoke
# ============================================================

@pytest.mark.ui
def test_home_page_loads(driver):

    home_page = HomePage(driver)

    home_page.open(
        "https://automationintesting.online/"
    )

    assert "Restful-booker-platform demo" in driver.title


# ============================================================
# HM-02: Verify navigation is visible
# Type: Positive / UI Functional
# ============================================================

@pytest.mark.ui
def test_navigation_is_visible(driver):

    home_page = HomePage(driver)

    home_page.open(
        "https://automationintesting.online/"
    )

    assert home_page.is_navigation_visible(), \
        "Main navigation is not visible"


# ============================================================
# HM-03: Verify hotel heading is visible
# Type: Positive / UI Functional
# ============================================================

@pytest.mark.ui
def test_hotel_heading_is_visible(driver):

    home_page = HomePage(driver)

    home_page.open(
        "https://automationintesting.online/"
    )

    assert home_page.is_hotel_heading_visible(), \
        "Hotel heading is not visible"