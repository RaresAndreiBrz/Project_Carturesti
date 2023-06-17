from locators.payment_page_locators import PaymentPageLocators
from pages.base_page import BasePage


class PaymentPage(BasePage):

    def go_to_summary_page(self):
        self.driver.find_element(*PaymentPageLocators.GO_TO_SUMMARY).click()

    def select_cash_on_receiving_option(self):
        self.driver.find_element(*PaymentPageLocators.CASH_BTN).click()

    def select_onlineCard_option(self):
        self.driver.find_element(*PaymentPageLocators.CARD_ONLINE_BTN).click()

    def select_order_payment_option(self):
        self.driver.find_element(*PaymentPageLocators.PAYMENT_ORDER_BTN).click()