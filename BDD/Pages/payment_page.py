import time

from locators.payment_page_locators import PaymentPageLocators
from Pages.base_page import BasePage


class PaymentPage(BasePage):

    def go_to_summary_page(self):
        btn = self.wait_for_clickable_element(PaymentPageLocators.GO_TO_SUMMARY)
        btn.click()

    def select_cash_on_receiving_option(self):
        time.sleep(2)
        btn = self.wait_for_clickable_element(PaymentPageLocators.CASH_BTN)
        btn.click()