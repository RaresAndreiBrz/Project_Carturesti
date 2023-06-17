from selenium.webdriver.common.by import By

from locators.login_second_page_locs import LoginSecondPageLocators
from pages.base_page import BasePage


class LoginSecondPage(BasePage):
    def send_wrong_mail_correct_pwd(self):
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).send_keys('andrei@gmail.comm')
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).send_keys('testingsite')

    def send_wrong_mail_wrong_pwd(self):
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).send_keys('andrei@gmail.comm')
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).send_keys('testingsiteee')

    def send_correct_mail_correct_pwd(self):
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).send_keys('andrei.rares.brz@gmail.com')
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).send_keys('testingsite')

    def send_correct_mail_wrong_pwd(self):
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.EMAIL_LOCATION_INPUT).send_keys('andrei.rares.brz@gmail.com')
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).clean()
        self.driver.find_element(*LoginSecondPageLocators.PWD_LOCATION_INPUT).send_keys('testingsiteee')

    def click_on_auth_btn(self):
        self.driver.find_element(*LoginSecondPageLocators.AUTH_BTN).click()