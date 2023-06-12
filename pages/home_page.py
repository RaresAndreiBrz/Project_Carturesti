import time

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):


    def click_login_button(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_LOGIN)
        button.click()

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


    def check_sign_up_succesfully(self):
        msg_to_check = self.wait_for_clickable_element(HomePageLocators.SIGNUP_SUCCESS_MSG)
        assert msg_to_check.is_displayed(), "Signup failed"


    def select_existing_user(self):
        button = self.wait_for_clickable_element(HomePageLocators.BTN_EXISTING_USER)
        button.click()


    def check_signing_in_succesfully(self):
        acc_new_btn = self.wait_for_clickable_element(HomePageLocators.BTN_CONT_SALUT)
        assert acc_new_btn.is_displayed(), "Nu apare butonul 'contul tau'"

    def check_wrong_pwd_mail_mssg(self):
        msg_pwd_fail_check = self.wait_for_clickable_element(HomePageLocators.BTN_AUTH)
        assert msg_pwd_fail_check.is_displayed(), "Nu mai esti pe login form"

    def send_text_to_search_bar(self,text_to_search):
        time.sleep(1)
        self.driver.find_element(*HomePageLocators.SEARCH_BAR).send_keys(text_to_search)


    def submit_search_text(self):
        search_bar = self.wait_for_clickable_element(HomePageLocators.BTN_SEARCH_LOOP)
        search_bar.click()

    def login_procedure(self):
        self.click_login_button()
        self.select_existing_user()
        self.complete_mail_for_login()
        self.complete_pwd_for_login()
        self.click_on_auth_button()
