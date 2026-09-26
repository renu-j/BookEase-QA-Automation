import pytest


@pytest.mark.ui
def test_screenshot_demo(driver):
    driver.get("https://automationintesting.online/")

    # Intentional failure — only to verify screenshot capture
    assert False, "Intentional failure to test automatic screenshot"