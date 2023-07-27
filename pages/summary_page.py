from locators.summary_page_locators import ConfirmationPageLocators
from Pages.base_page import BasePage


class SummaryPage(BasePage):
    def finish_order(self):
        self.driver.find_element(*ConfirmationPageLocators.FINISH_ORDER).click()

    def complete_observations(self):
        self.wait_for_displayed_element(ConfirmationPageLocators.OBSERVATIONS_INPUT).send_keys("ANULATI ACEASTA "
                                                                                               "COMANDA AUTOMATA")

    def select_gift_items(self):
        self.driver.find_element(*ConfirmationPageLocators.PACK_GIFT_OPTION).click()

    def select_gift_all_items(self):
        self.driver.find_element(*ConfirmationPageLocators.PACK_ALL_PRODUCTS).click()

