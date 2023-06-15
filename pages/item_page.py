from locators.item_page_locators import ItemPageLocators
from pages.base_page import BasePage

class ItemPage(BasePage):

    def go_back(self):
        self.back()

    def multiply_clicks_on_add(self, multiplier):
        for click in range(multiplier):
            self.driver.find_element(*ItemPageLocators.BTN_ADD_PRODUS).click()