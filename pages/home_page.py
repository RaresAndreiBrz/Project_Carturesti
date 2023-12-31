import time
from selenium.webdriver import ActionChains
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def click_login_button(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_LOGIN)
        button.click()

    def cancel_cookie(self):
        self.driver.find_element(*HomePageLocators.CANCEL_COOKIE_BTN).click()

    def complete_mail_for_login(self):
        button = self.wait_for_clickable_element(HomePageLocators.SIGN_IN_EMAIL_INPUT)
        button.send_keys("andrei.rares.brz@gmail.com")

    def complete_wrong_mail_for_login(self):
        button = self.wait_for_clickable_element(HomePageLocators.SIGN_IN_EMAIL_INPUT)
        button.send_keys("andreiraresbrz@gmail.com")

    def complete_pwd_for_login(self):
        button = self.wait_for_clickable_element(HomePageLocators.SIGN_IN_PWD_INPUT)
        button.send_keys("testingsite")

    def complete_wrong_pwd_for_login(self):
        button = self.wait_for_clickable_element(HomePageLocators.SIGN_IN_PWD_INPUT)
        button.send_keys("Testingsite")

    def complete_mail_for_signup(self):
        button = self.wait_for_clickable_element(HomePageLocators.SIGN_UP_EMAIL_INPUT)
        button.send_keys(HomePageLocators.MAIL_for_USER)

    def complete_pwd_for_signup(self):
        button = self.wait_for_clickable_element(HomePageLocators.SIGN_UP_PWD_INPUT)
        button.send_keys(HomePageLocators.PWD_for_USER)

    def select_new_user(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_NEW_USER)
        button.click()

    def click_recaptcha_box(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_BOX_RECAPTCHA)
        button.click()

    def click_on_auth_button(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_AUTH)
        button.click()
        time.sleep(1)

    def check_sign_up_succesfully(self):
        msg_to_check = self.wait_for_clickable_element(HomePageLocators.SIGNUP_SUCCESS_MSG)
        assert msg_to_check.is_displayed(), "Signup failed"

    def select_existing_user(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_EXISTING_USER)
        button.click()

    def check_signing_in_succesfully(self):
        acc_new_btn = self.driver.find_element(*HomePageLocators.BTN_CONT_SALUT)
        assert acc_new_btn.is_displayed(), "Button 'CONTUL TAU' doesn`t show up"

    def check_wrong_pwd_mail_mssg(self):
        msg_pwd_fail_check = self.wait_for_displayed_element(HomePageLocators.BTN_AUTH)
        assert msg_pwd_fail_check.is_displayed() == True, "You are not on login form"

    def send_text_to_search_bar(self, text_to_search):
        time.sleep(1)
        self.driver.find_element(*HomePageLocators.SEARCH_BAR).send_keys(text_to_search)

    def submit_search_text(self):
        search_bar = self.wait_for_clickable_element(HomePageLocators.BTN_SEARCH_LOOP)
        search_bar.click()
        time.sleep(1)

    def login_procedure(self):
        self.click_login_button()
        self.select_existing_user()
        self.complete_mail_for_login()
        self.complete_pwd_for_login()
        self.click_on_auth_button()

    def check_error_of_missing_product(self):
        mssg_to_check = self.driver.find_element(*HomePageLocators.MESSAGE_ERROR_PRODUCT_NOT_FOUND)
        assert mssg_to_check.is_displayed(), 'The error message for missing items does not exist.'

    def click_on_my_account_btn(self):
        self.driver.find_element(*HomePageLocators.BTN_CONT_SALUT).click()

    def click_on_wishlist_btn(self):
        self.driver.find_element(*HomePageLocators.BTN_CONT_WISHLIST).click()
        time.sleep(1)

    def go_to_return_policy(self):
        self.wait_for_clickable_element(HomePageLocators.RETURN_POLICY_PAGE_LINK).click()

    def click_on_products_inventory(self):
        self.wait_for_clickable_element(HomePageLocators.BTN_PRODUCTS).click()
        time.sleep(0.5)

    def put_cursor_on_music_category(self):
        self.music_btn = self.wait_for_clickable_element(HomePageLocators.MUSIC_CATEGORY)
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.music_btn)

    def put_cursor_on_disney_category(self):
        self.disney_btn = self.wait_for_clickable_element(HomePageLocators.DISNEY_CATEGORY)
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(self.disney_btn)

    def check_second_list_displayed(self):
        self.list_items = self.wait_for_displayed_element(HomePageLocators.BOX_OF_CATEGORY_LIST)
        assert self.list_items.is_displayed(), "Items of the music category not displayed"

    def go_to_assistance_page(self):
        self.wait_for_clickable_element(HomePageLocators.GO_TO_ASSISTANCE_PAGE).click()

    def check_categories_list_is_displayed(self):
        self.list = self.driver.find_element(*HomePageLocators.BOX_OF_PRODUCTS_LIST)
        assert self.list.is_displayed(), 'List of categories not displayed'
