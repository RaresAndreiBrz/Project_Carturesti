import time

from locators.item_page_locators import ItemPageLocators
from Pages.base_page import BasePage


class ItemPage(BasePage):

    def go_back(self):
        self.back()

    def multiply_clicks_on_add(self, multiplier):
        for click in range(multiplier):
            self.driver.find_element(*ItemPageLocators.BTN_ADD_PRODUCT_IN_CART).click()

    def check_details_displayed_box(self):
        self.box = self.driver.find_element(*ItemPageLocators.DETAILS_BOX)
        assert self.box.is_displayed(), 'Details not displayed'

    def add_product_to_wishlist(self):
        time.sleep(0.2)
        self.driver.find_element(*ItemPageLocators.BTN_ADD_PRODUCT_IN_WISHLIST).click()
        time.sleep(0.2)
        self.driver.find_element(*ItemPageLocators.BTN_ADD_PRODUCT_IN_WISHLIST_2).click()
