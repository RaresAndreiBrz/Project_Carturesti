import time

from locators.delivery_page_locators import DeliveryPageLocators
from Pages.base_page import BasePage


class DeliveryPage(BasePage):


    def click_on_persoana_fizica(self):
        self.wait_for_displayed_element(DeliveryPageLocators.INDIVIDUAL_OPTION).click()

    def go_to_payment_page(self):
        self.driver.find_element(*DeliveryPageLocators.TOWARDS_PAYMENT_BTN).click()
        time.sleep(1)

    def send_wrong_inputs(self):
        self.driver.find_element(*DeliveryPageLocators.FIRST_NAME_INPUT).send_keys(' ')
        self.driver.find_element(*DeliveryPageLocators.LAST_NAME_INPUT).send_keys(' ')
        self.driver.find_element(*DeliveryPageLocators.POSTAL_CODE_INPUT).send_keys("000")
        self.driver.find_element(*DeliveryPageLocators.ADDRESS_TEXT_INPUT).send_keys('AAA')
        self.driver.find_element(*DeliveryPageLocators.CITY_DROP_INPUT).click()
        self.driver.find_element(*DeliveryPageLocators.CITY_DROP_INPUT_BUCURESTI).click()

    def send_correct_inputs(self):
        self.driver.find_element(*DeliveryPageLocators.FIRST_NAME_INPUT).send_keys('jkb')
        self.driver.find_element(*DeliveryPageLocators.LAST_NAME_INPUT).send_keys('sadasd')
        self.driver.find_element(*DeliveryPageLocators.PHONE_NR_INPUT).send_keys('+40767000000')
        self.driver.find_element(*DeliveryPageLocators.POSTAL_CODE_INPUT).send_keys('000000')
        self.driver.find_element(*DeliveryPageLocators.ADDRESS_TEXT_INPUT).send_keys('ADRS')
        time.sleep(0.3)
        self.driver.find_element(*DeliveryPageLocators.CITY_DROP_INPUT).click()
        time.sleep(0.3)
        self.driver.find_element(*DeliveryPageLocators.CITY_DROP_INPUT_BUCURESTI).click()
        time.sleep(0.3)
        self.driver.find_element(*DeliveryPageLocators.TOWN_DROP_INPUT).click()
        time.sleep(0.3)
        self.driver.find_element(*DeliveryPageLocators.TOWN_DROP_INPUT_SECTOR).click()
        time.sleep(0.3)
        try:
            self.driver.find_element(*DeliveryPageLocators.COUNTRY_DROP_INPUT).click()
            self.driver.find_element(*DeliveryPageLocators.COUNTRY_DROP_INPUT_ROMANIA).click()
        except:
            pass


    def stabileste_transport_cu_bicicleta(self):
        try:
            self.driver.find_element(*DeliveryPageLocators.BYCICLE_TRANSPORT_OPTION).click()
        except:
            pass
