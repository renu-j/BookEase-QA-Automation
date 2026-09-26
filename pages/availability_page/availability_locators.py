from selenium.webdriver.common.by import By


CHECK_IN = (
    By.XPATH,
    "//label[@for='checkin']/following-sibling::div//input"
)

CHECK_OUT = (
    By.XPATH,
    "//label[@for='checkout']/following-sibling::div//input"
)

CHECK_AVAILABILITY_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Check Availability']"
)