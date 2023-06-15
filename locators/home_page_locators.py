from selenium.webdriver.common.by import By


class HomePageLocators:


    BTN_LOGIN = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[2]/button/span")
    BTN_NEW_USER = (By.ID, "signupTrigger")
    BTN_EXISTING_USER = (By.XPATH, '//button[@id="loginTrigger"]')

    SIGN_IN_EMAIL_INPUT = (By.ID, "loginform-email")
    SIGN_UP_EMAIL_INPUT = (By.ID, "signupform-email")
    SIGN_IN_PWD_INPUT = (By.ID, "loginform-password")
    SIGN_UP_PWD_INPUT = (By.ID, "signupform-password")
    MAIL_for_USER = "testing@gmail.comm"
    PWD_for_USER = "testingsite"
    BTN_BOX_RECAPTCHA = (By.XPATH, '//*[@id="rc-anchor-container"]/div[3]/div[1]/div')
    BTN_AUTH = (By.XPATH, '//*[@id="modalLoginForm"]/div[3]/button')

    SIGNUP_SUCCESS_MSG = (By.ID, "w2-success")
    SIGNUP_SUCCESS_MSG_TEXT = "Inregistrarea a fost realizata cu succes. Am trimis un email de confirmare către adresa furnizata."
    RECAPTCHA_ERROR = (By.CLASS_NAME, "rc-anchor-error-msg")
    RECAPTCHA_ERROR_MSG = "Confirmarea a expirat. Bifează din nou caseta de selectare."
    RECAPTCHA_ALERT_MSG = (By.CLASS_NAME, "help-block md-input-message-animation")
    RECAPTCHA_ALERT_MSG_TEXT = "Acest câmp trebuie completat."
    ALERT_MSG_WRONG_MAILorPWD = (By.CLASS_NAME, "help-block md-input-message-animation")
    ALERT_MSG = "Acest câmp trebuie completat."

    SEARCH_BAR = (By.ID, "search-input")
    BTN_SEARCH_LOOP = (By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[2]/i")
    CART_ITEMS_NUMBER = (By.XPATH, '//*[@data-ng-bind="cart.count()"]')
    BTN_CART = (By.CLASS_NAME, "checkout__button")
    BTN_REMOVE_FIRST_ITEM = (By.XPATH, "//tr[1]/td[3]/a/i")
    BTN_CONT_SALUT = (By.XPATH, '//*[@id="accountDropdown"]')
    BTN_CONT_CONTU_TAU = (By.PARTIAL_LINK_TEXT, "CONTUL")
    BTN_CONT_MODIF_PWD = (By.PARTIAL_LINK_TEXT, "MODIFICARE")
    BTN_CONT_WISHLIST = (By.PARTIAL_LINK_TEXT, "WISHLIST")
    BTN_CONT_LOGOUT = (By.PARTIAL_LINK_TEXT, "LOGOU")
    BTN_GOOGLE_LOGIN = (By.CLASS_NAME, "google auth-link")
    BTN_FB_LOGIN = (By.CLASS_NAME, "facebook auth-link")
    CART_EMPTY_MSSG = (By.CLASS_NAME, "checkout__empty ng-scope")
    CART_EMPTY_MSSG_TEXT = "Nu aveți produse în coș."  # in html textul e urmat de spatii
    BTN_ASISTENTA = (By.CLASS_NAME, "md-button asistenta")
    BTN_LOGO_HOMEPAGE = (By.CLASS_NAME, "logo-cartu")
    BTN_ASIST_LIVE = (By.ID, "druidContainerTooltip")
    BTN_CARTURESTI = (By.ID, "carturestiDropdown")  # butonul cu 3 items de langa login btn
    BTN_CARTURESTI_DESPRE_NOI = (By.CLASS_NAME, "dropdown-toggle md-button md-ink-ripple")
    BTN_CARTURESTI_BLOG = (
    By.CLASS_NAME, "/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[3]/a")
    BTN_CARTURESTI_LIBRARII = (
    By.CLASS_NAME, "/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[2]/a")
    BTN_PRODUSE = (By.ID, "buton-produse")
    MESSAGE_ERROR_PRODUCT_NOT_FOUND = (By.XPATH, '//*[@id="search-category"]')