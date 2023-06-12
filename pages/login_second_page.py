from selenium.webdriver.common.by import By


class LoginSecondPage():
    SIGN_IN_PAGE_EMAIL_INPUT = (By.ID, "loginform-email")
    SIGN_IN_PAGE_PWD_INPUT = (By.ID, "loginform-password")
    BTN_AUTH_LOGIN_PAGE = (By.CLASS_NAME, "md-button md-raised pull-right")