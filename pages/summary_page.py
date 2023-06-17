from locators.summary_page_locators import ConfirmationPageLocators
from pages.base_page import BasePage


class SummaryPage(BasePage):
    def finish_order(self):
        self.driver.find_element(*ConfirmationPageLocators.FINISH_ORDER).click()

    def complete_observations(self):
        self.driver.find_element(*ConfirmationPageLocators.OBSERVATIONS_INPUT).send_keys("ANULATI ACEASTA COMANDA AUTOMATA")

    def select_impachetare_all_items(self):
        self.driver.find_element(*ConfirmationPageLocators.PACK_GIFT_OPTION).click()
        self.driver.find_element(*ConfirmationPageLocators.PACK_ALL_PRODUCTS).click()

    def select_impachetare_items_separately(self):
        self.driver.find_element(*ConfirmationPageLocators.PACK_GIFT_OPTION).click()
        self.driver.find_element(*ConfirmationPageLocators.PACK_PRODUCTS_SEPARATELY).click()