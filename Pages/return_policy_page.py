from locators.return_policy_page_locators import ReturnPolicyPageLocators
from Pages.base_page import BasePage


class ReturnPolicyPage(BasePage):

    def check_title_is_displayed(self):
        self.title = self.driver.find_element(*ReturnPolicyPageLocators.TITLE_OF_POLICY)
        assert self.title.is_displayed(), 'Title not seen'

    def check_text_is_displayed(self):
        self.text = self.driver.find_element(*ReturnPolicyPageLocators.TEXT_OF_POLICY)
        assert self.text.is_displayed(), 'Text not seen'
