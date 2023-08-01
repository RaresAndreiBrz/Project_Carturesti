import time
from locators.wishlist_page_locators import WishlistPageLocators
from pages.base_page import BasePage


class WishlistPage(BasePage):


    def check_presence_of_products_in_wishlist(self):
        self.list_of_products = self.driver.find_elements(*WishlistPageLocators.LIST_OF_PRODUCTS)
        assert len(self.list_of_products) > 0, "NO products in wishlist"

    def remove_products_from_wishlists(self):
        self.buttons_for_remove = self.driver.find_element(*WishlistPageLocators.REMOVE_BUTTONS)
        self.buttons_for_remove.click()
        time.sleep(2)
        self.driver.find_element(*WishlistPageLocators.REMOVE_CONFIRM).click()
        time.sleep(2)

