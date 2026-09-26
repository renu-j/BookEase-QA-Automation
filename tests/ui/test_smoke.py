def test_home_page_loads(driver):
    """
    Test Type: Smoke Test
    Feature: Home Page
    Purpose: Verify that the application is accessible
             and the home page loads successfully.
    """

    driver.get("https://automationintesting.online/")

    # Expected: Application home page should load successfully
    assert "Restful-booker-platform demo" in driver.title
