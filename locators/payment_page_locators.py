from selenium.webdriver.common.by import By


class PaymentPageLocators:

    GO_TO_SUMMARY = (By.XPATH, '//*[@class="md-accent md-raised md-button md-default-theme pull-right checkout-submit-btn"]')

    CASH_BTN = (By.XPATH, '//*[@for="pmed-1"]')
    CARD_ONLINE_BTN = (By.XPATH, '//*[@for="pmed-4"]')
    PAYMENT_ORDER_BTN = (By.XPATH, '//*[@for="pmed-2"]')