from selenium.webdriver.common.by import By


class LoginSecondPageLocators():
    EMAIL_LOCATION_INPUT = (By.XPATH, "//div[@class='input-group']//input[@id='loginform-email']")
    PWD_LOCATION_INPUT = (By.XPATH, "//div[@class='input-group']//input[@id='loginform-password']")
    AUTH_BTN = (By.XPATH, '//*[@class="md-button md-raised pull-right"]')

    PWD_OR_MAIL_ERROR = (By.XPATH, '//*[@id="login-form"]/div[2]/div[2]')
