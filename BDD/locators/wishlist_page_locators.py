from selenium.webdriver.common.by import By


class WishlistPageLocators:
    INPUT_NAME_NEW_WISHLIST = (By.XPATH, '//*[@id="wishlist-name"]')
    CREATE_NEW_WISHLIST_BTN = (By.XPATH, '//*[@class="btn"]')
    LIST_OF_PRODUCTS = (By.XPATH, '//*[@class="md-headline ng-binding"]')
    REMOVE_BUTTONS = (By.XPATH, '//*[@aria-label="Remove wishlist"]')
    REMOVE_CONFIRM = (By.XPATH, "//button[@ng-click='hide()']")
