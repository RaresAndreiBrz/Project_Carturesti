import time
from locators.delivery_page_locators import DeliveryPageLocators
from pages.base_page import BasePage

class DeliveryPage(BasePage):

    def click_on_persoana_fizica(self):
        time.sleep(0.5)
        self.driver.find_element(*DeliveryPageLocators.INDIVIDUAL_OPTION).click()

    def click_on_add_address(self):
        time.sleep(1)
        self.driver.find_element(*DeliveryPageLocators.ADD_ADDRESS).click()
        time.sleep(1)

    def go_to_payment_page(self):
        i = 0
        while i<10:
            try:
                self.establish_free_transport()
                self.driver.find_element(*DeliveryPageLocators.TOWARDS_PAYMENT_BTN).click()
            except:
                self.establish_free_transport()
                self.driver.find_element(*DeliveryPageLocators.TOWARDS_PAYMENT_BTN).click()
            time.sleep(50)
            if "billing" in self.driver.current_url:
                break
            i+=1

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


    def establish_transport_with_bike(self):
        try:
            self.establish_fast_delivery_transport()
            self.driver.find_element(*DeliveryPageLocators.BYCICLE_TRANSPORT_OPTION).click()
        except:
            pass

    def establish_free_transport(self):
        # self.establish_fast_delivery_transport()
        self.driver.find_element(*DeliveryPageLocators.FREE_TRANSPORT_OPTION).click()
        # try:
        #     self.establish_fast_delivery_transport()
        #     self.driver.find_element(*DeliveryPageLocators.FREE_TRANSPORT_OPTION).click()
        # except:
        #     pass

    def establish_fast_delivery_transport(self):
        self.driver.find_element(*DeliveryPageLocators.FAST_DELIVERY_TRANSPORT_OPTION).click()
        try:
            self.driver.find_element(*DeliveryPageLocators.FAST_DELIVERY_TRANSPORT_OPTION).click()
        except:
            pass

