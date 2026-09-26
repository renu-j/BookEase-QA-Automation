from selenium.webdriver.common.by import By


ROOMS_SECTION = (
    By.ID,
    "rooms"
)

ROOM_CARDS = (
    By.CSS_SELECTOR,
    "#rooms .card"
)

ROOM_TITLES = (
    By.CSS_SELECTOR,
    "#rooms .card-title"
)

SINGLE_ROOM_BOOK_NOW = (
    By.XPATH,
    "//section[@id='rooms']"
    "//div[contains(@class,'room-card')][.//*[normalize-space()='Single']]"
    "//a[contains(normalize-space(), 'Book now')]"
)