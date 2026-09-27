import pytest


@pytest.mark.ai_demo
def test_screenshot_demo(driver):
    driver.get("https://automationintesting.online/")

    # Intentional failure — only for AI failure-analysis demonstration
    assert False, "Intentional failure to test automatic screenshot and AI failure analysis"