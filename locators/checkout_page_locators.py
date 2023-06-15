from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    PRICES_OF_INDIVIDUAL_ITEMS = (By.XPATH, '// *[ @data-label="Preț"]')    #LIST
    TOTAL_PRICE_OF_EACH_ITEM = (By.XPATH, '// *[ @data-label="Total"]')    #LIST
    TOTAL_PRICE_TO_PAY = (By.XPATH, '//*[@id="checkout-products-grid-container"]/table/tfoot/tr/td[7]')
    PRODUCTS_NAMES = (By.XPATH, '//*[@class="coloanaProdus kv-align-middle"]')
    ITEMS_SELECTED = (By.XPATH, '//*[@class="form-control" and @type="number"]')
    DATE_DE_LIVRARE_BTN = (By.XPATH, '//*[@class="md-accent md-raised md-button md-default-theme pull-right next-btn"]')

    REMOVE_BUTTONS = (By.XPATH, '//*[@title="Șterge"]')