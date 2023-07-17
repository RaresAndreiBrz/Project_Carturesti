from selenium.webdriver.common.by import By


class HomePageLocators:
    #cookie locs
    CANCEL_COOKIE_BTN = (By.XPATH, '/html/body/div[3]/button')

    #log locs
    BTN_LOGIN = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[2]/button/span")
    BTN_NEW_USER = (By.ID, "signupTrigger")
    BTN_EXISTING_USER = (By.XPATH, '//button[@id="loginTrigger"]')
    BTN_AUTH = (By.XPATH, '//*[@id="modalLoginForm"]/div[3]/button')
    BTN_GOOGLE_LOGIN = (By.CLASS_NAME, "google auth-link")
    BTN_FB_LOGIN = (By.CLASS_NAME, "facebook auth-link")

    # signin locs
    SIGN_IN_EMAIL_INPUT = (By.ID, "loginform-email")
    SIGN_UP_EMAIL_INPUT = (By.ID, "signupform-email")
    SIGN_IN_PWD_INPUT = (By.ID, "loginform-password")

    # signup locs
    SIGN_UP_PWD_INPUT = (By.ID, "signupform-password")
    MAIL_for_USER = "testing@gmail.comm"
    PWD_for_USER = "testingsite"
    SIGNUP_SUCCESS_MSG = (By.ID, "w2-success")
    SIGNUP_SUCCESS_MSG_TEXT = "Inregistrarea a fost realizata cu succes. Am trimis un email de confirmare către adresa furnizata."

    # recaptcha locs
    BTN_BOX_RECAPTCHA = (By.XPATH, '//*[@id="rc-anchor-container"]/div[3]/div[1]/div')
    RECAPTCHA_ERROR = (By.CLASS_NAME, "rc-anchor-error-msg")
    RECAPTCHA_ERROR_MSG = "Confirmarea a expirat. Bifează din nou caseta de selectare."
    RECAPTCHA_ALERT_MSG = (By.CLASS_NAME, "help-block md-input-message-animation")
    RECAPTCHA_ALERT_MSG_TEXT = "Acest câmp trebuie completat."

    #alerts locs
    ALERT_MSG_WRONG_MAILorPWD = (By.CLASS_NAME, "help-block md-input-message-animation")
    ALERT_MSG = "Acest câmp trebuie completat."

    #menu buttons
    SEARCH_BAR = (By.ID, "search-input")
    BTN_SEARCH_LOOP = (By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[2]/i")
    BTN_CARTURESTI = (By.ID, "carturestiDropdown")  # butonul cu 3 items de langa login btn
    BTN_CARTURESTI_ABOUT_US = (By.CLASS_NAME, "dropdown-toggle md-button md-ink-ripple")
    BTN_CARTURESTI_BLOG = (
        By.CLASS_NAME, "/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[3]/a")
    BTN_CARTURESTI_LIBRARIES = (
        By.CLASS_NAME, "/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[2]/a")
    BTN_PRODUCTS = (By.ID, "buton-produse")

    #cart menu
    BTN_CART = (By.CLASS_NAME, "checkout__button")
    CART_PRODUCTS_NUMBER = (By.XPATH, '//*[@data-ng-bind="cart.count()"]')
    BTN_REMOVE_FIRST_PRODUCT = (By.XPATH, "/html/body/div[2]//div/div[2]//td[3]/a/i")
    CART_EMPTY_MSSG = (By.CLASS_NAME, "checkout__empty ng-scope")
    CART_EMPTY_MSSG_TEXT = "Nu aveți produse în coș."  # in html textul e urmat de spatii

    #buttons my_account
    BTN_CONT_SALUT = (By.XPATH, '//*[@id="accountDropdown"]')
    BTN_CONT_CONTU_TAU = (By.PARTIAL_LINK_TEXT, "CONTUL")
    BTN_CONT_MODIF_PWD = (By.PARTIAL_LINK_TEXT, "MODIFICARE")
    BTN_CONT_WISHLIST = (By.PARTIAL_LINK_TEXT, "WISHLIST")
    BTN_CONT_LOGOUT = (By.PARTIAL_LINK_TEXT, "LOGOU")

    #buttons from home_page
    MESSAGE_ERROR_PRODUCT_NOT_FOUND = (By.XPATH, '//*[@id="search-category"]')
    RETURN_POLICY_PAGE_LINK = (By.XPATH, "//a[normalize-space()='Politica de retur']")
    BOX_OF_CATEGORY_LIST = (By.XPATH, '//*[@id="menuCanvas"]')
    BOX_OF_PRODUCTS_LIST = (By.XPATH, '//*[@id="menuCanvas"]')
    MUSIC_CATEGORY = (By.XPATH, "//md-list-item[@role='listitem']//a[contains(text(),'Muzica')]")
    DISNEY_CATEGORY = (By.XPATH, "//a[normalize-space()='Disney']")
    GO_TO_ASSISTANCE_PAGE = (By.XPATH, "//body/footer/div/div[@role='contentinfo']/div/ul/li[4]/a[1]")
