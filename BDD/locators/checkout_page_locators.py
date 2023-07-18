from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    TOTAL_PRICE_OF_EACH_ITEM = (By.XPATH, '// *[ @data-label="Total"]')    #LIST
    TOTAL_PRICE_TO_PAY = (By.XPATH, '//*[@id="checkout-products-grid-container"]/table/tfoot/tr/td[7]')
    GO_TO_DELIVERY_PAGE_BTN = (By.CSS_SELECTOR, '#checkout-products-grid-pjax > div.pull-right > a')
    REMOVE_PRODUCTS_BUTTONS = (By.XPATH, '//*[@title="Șterge"]')