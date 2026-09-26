
import os

import pytest
from selenium import webdriver

from utils.ai_failure_analyzer import analyze_failure


@pytest.fixture
def driver(request):
    driver = webdriver.Edge()
    driver.maximize_window()

    yield driver

    # ---------------------------------------------------------
    # Capture failure evidence
    # ---------------------------------------------------------
    if request.node.rep_call.failed:

        # Create report folders if they do not exist
        os.makedirs("reports/screenshots", exist_ok=True)
        os.makedirs("reports/ai", exist_ok=True)

        # -----------------------------------------------------
        # 1. Save screenshot
        # -----------------------------------------------------
        screenshot_path = (
            f"reports/screenshots/{request.node.name}.png"
        )

        driver.save_screenshot(screenshot_path)

        # -----------------------------------------------------
        # 2. Get failure information
        # -----------------------------------------------------
        error_message = str(
            request.node.rep_call.longrepr
        )

        # -----------------------------------------------------
        # 3. Analyze failure
        # -----------------------------------------------------
        analysis = analyze_failure(
            request.node.name,
            error_message
        )

        # -----------------------------------------------------
        # 4. Save AI analysis
        # -----------------------------------------------------
        analysis_path = (
            f"reports/ai/{request.node.name}.txt"
        )

        with open(
            analysis_path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(analysis)

    # ---------------------------------------------------------
    # Close browser
    # ---------------------------------------------------------
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Make the pytest result available to the fixture.
    """
    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )

