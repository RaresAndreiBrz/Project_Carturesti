import random

from locators.checkout_page_locators import CheckoutPageLocators
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def check_amount_to_pay_for_all_products(self):

        total_on_cart_text = self.driver.find_element(*CheckoutPageLocators.TOTAL_PRICE_TO_PAY).text
        total_on_cart = float(total_on_cart_text.replace(',', '.').replace('RON', ''))

        list_prices = self.driver.find_elements(*CheckoutPageLocators.TOTAL_PRICE_OF_EACH_ITEM)
        full_price_to_pay = 0
        for item in list_prices:
            full_price_to_pay += float(item.text.replace(',','.').replace('RON', ''))
        assert full_price_to_pay == total_on_cart, "Wrong amount to pay!"

    def go_to_delivery_page(self):
        self.driver.find_element(*CheckoutPageLocators.GO_TO_DELIVERY_PAGE_BTN).click()

    def random_remove(self):
        remove_buttons = self.driver.find_elements(*CheckoutPageLocators.REMOVE_PRODUCTS_BUTTONS)
        random_choice = random.choice(remove_buttons)
        random_choice.click()