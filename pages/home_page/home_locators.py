from selenium.webdriver.common.by import By


ROOMS_LINK = (
    By.CSS_SELECTOR,
    'a[href="#rooms"]'
)

ROOMS_SECTION = (
    By.ID,
    "rooms"
)

NAVIGATION = (
    By.CSS_SELECTOR,
    "nav"
)

HOTEL_HEADING = (
    By.XPATH,
    "//h1[contains(normalize-space(), 'Welcome to Shady Meadows B&B')]"
)