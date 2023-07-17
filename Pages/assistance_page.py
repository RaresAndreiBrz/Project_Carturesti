from locators.assistance_page_locators import AssistancePageLocators
from Pages.base_page import BasePage


class AssistancePage(BasePage):
    def check_buttons_nr_equal_with_text_boxes(self):
        self.buttons = self.driver.find_elements(*AssistancePageLocators.BUTTONS)
        self.boxes_with_text = self.driver.find_elements(*AssistancePageLocators.BOXES_WITH_INFO)
        assert len(self.buttons) + 1 == len(
            self.boxes_with_text), "There is a difference regarding number of buttons and number of text boxes"
