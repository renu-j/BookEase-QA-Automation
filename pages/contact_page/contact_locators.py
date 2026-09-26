from selenium.webdriver.common.by import By


NAME = (
    By.ID,
    "name"
)

EMAIL = (
    By.ID,
    "email"
)

PHONE = (
    By.ID,
    "phone"
)

SUBJECT = (
    By.ID,
    "subject"
)

MESSAGE = (
    By.ID,
    "description"
)

SUBMIT_BUTTON = (
    By.CSS_SELECTOR,
    "#contact button.btn.btn-primary[type='button']"
)

SUCCESS_MESSAGE = (
    By.XPATH,
    "//h3[contains(normalize-space(), 'Thanks for getting in touch')]"
)

VALIDATION_ALERT = (
    By.CSS_SELECTOR,
    "#contact div.alert.alert-danger"
)