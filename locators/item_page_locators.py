from selenium.webdriver.common.by import By


class ItemPageLocators:
    BTN_ADD_PRODUCT_IN_CART = (By.XPATH, '//*[@title="Adaugă în coș"]')
    BTN_ADD_PRODUCT_IN_WISHLIST = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/md-card/md-card-content/div[1]/a")
    BTN_ADD_PRODUCT_IN_WISHLIST_2 = (By.XPATH, '//*[@class="wList ng-scope"]')
    BTN_CONTACT = (By.PARTIAL_LINK_TEXT, "ontacteaz")

    DETAILS_BOX = (By.XPATH, '//*[@class="row detailsContainer"]')
