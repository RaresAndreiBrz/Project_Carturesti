from selenium.webdriver.common.by import By


class ConfirmationPageLocators:
    OFFERS_AND_DISCOUNTS = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/md-checkbox/div[1]/div')
    TOTAL_AMOUNT_TO_PAY_FOR_ORDER = (By.XPATH, '//*[@class="totalPrice pull-right"]')
    TOTAL_AMOUNT_OF_PRODUCTS_TO_PAY = (By.XPATH, '//*[@data-label="Total"]')
    TOTAL_AMOUNT_OF_TRANSPORT_TO_PAY = (By.XPATH, '//*[@class="shippingText"]')
    ORDER_NUMBER = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/kbd')
    LOCATION_OF_CONFIRMATION = (By.XPATH, '//*[@class="col-sm-6"][1]')
    PARTIAL_MESSAGE_OF_CONFIRMATION_TEXT = "a fost înregistrată în sistem"
