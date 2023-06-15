from selenium.webdriver.common.by import By

class DeliveryPageLocators:
    ACASA_OPTION = (By.XPATH, '//*[@id="w3"]/li[1]/a/div')
    LIBRARIE_OPTION = (By.XPATH, '//*[@id="w3"]/li[2]/a/div')
    LOCKER_OPTION = (By.XPATH, '//*[@id="w3"]/li[3]/a/div')
    TOWARDS_PAYMENT_BTN = (By.XPATH, '//*[@id="shipping-form"]/div[4]/div[2]/button/text()')
    BACK_TO_CART_BTN = (By.XPATH, '//*[@id="shipping-form"]/div[4]/div[1]/a/text()')
