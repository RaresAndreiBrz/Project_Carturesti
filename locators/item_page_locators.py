from selenium.webdriver.common.by import By


class ItemPageLocators:
    BTN_ADD_PRODUS = (By.XPATH, '//*[@title="Adaugă în coș"]')
    BTN_ADD_WISHLIST = (By.CLASS_NAME, "clean-a")
    BTN_CONTACTEAZA = (By.PARTIAL_LINK_TEXT, "ontacteaz")