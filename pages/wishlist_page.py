from locators.wishlist_page_locators import WishlistPageLocators
from pages.base_page import BasePage


class WishlistPage(BasePage):

    def create_new_wishlist(self,wishlist_name):
        self.driver.find_element(*WishlistPageLocators.INPUT_NAME_NEW_WISHLIST).send_keys(wishlist_name)
        self.driver.find_element(*WishlistPageLocators.CREATE_NEW_WISHLIST_BTN).click()

    def check_presence_of_products_in_wishlist(self):
        self.list_of_products = self.driver.find_elements(*WishlistPageLocators.LIST_OF_PRODUCTS)
        assert len(self.list_of_products) > 0, "NO products on wishlist"

