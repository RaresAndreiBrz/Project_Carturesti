import time

from locators.delivery_page_locators import DeliveryPageLocators
from Pages.base_page import BasePage


class DeliveryPage(BasePage):
    def click_on_livrare_acasa(self):
        self.wait_for_displayed_element(DeliveryPageLocators.ACASA_OPTION).click()

    def click_on_library_option(self):
        self.wait_for_displayed_element(DeliveryPageLocators.LIBRARIE_OPTION).click()

    def click_on_libraria_afi(self):
        self.wait_for_displayed_element(DeliveryPageLocators.AFI_LOCATION_BUTTON).click()

    def click_on_locker_option(self):
        self.wait_for_displayed_element(DeliveryPageLocators.LOCKER_OPTION).click()

    def click_on_persoana_fizica(self):
        self.wait_for_displayed_element(DeliveryPageLocators.INDIVIDUAL_OPTION).click()

    def click_on_persoana_juridica(self):
        self.wait_for_displayed_element(DeliveryPageLocators.COMPANY_OPTION).click()

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

    def stabileste_transport_gratuit(self):
        try:
            self.driver.find_element(*DeliveryPageLocators.FREE_TRANSPORT_OPTION).click()
        except:
            pass

    def stabileste_transport_cu_bicicleta(self):
        try:
            self.driver.find_element(*DeliveryPageLocators.BYCICLE_TRANSPORT_OPTION).click()
        except:
            pass

    def stabileste_transport_curier_rapid(self):
        try:
            self.driver.find_element(*DeliveryPageLocators.FAST_DELIVERY_TRANSPORT_OPTION).click()
        except:
            pass

    def stabileste_transport_ambalaj_returnabil(self):
        try:
            self.driver.find_element(*DeliveryPageLocators.RETURNABLE_PACK_TRANSPORT_OPTION).click()
        except:
            pass

    def check_correct_amount_to_pay_from_delivery_page(self):
        suma_produse = self.driver.find_elements(*DeliveryPageLocators.TOTAL_PRICE_OF_PRODUCTS_FROM_CART)
        suma_produse_lei = 0
        suma_transport = self.driver.find_elements(*DeliveryPageLocators.TOTAL_TRANSPORT_COST).text
        suma_transport_lei = float(suma_transport.replace(',', '.').replace('RON', ''))
        suma_totala = self.driver.find_element(*DeliveryPageLocators.TOTAL_AMOUNT_TO_PAY).text
        suma_totala_lei = float(suma_totala.replace(',', '.').replace('RON', ''))
        for pret in suma_produse:
            suma_produse_lei += float(pret.text.replace(',', '.').replace('RON', ''))

        assert suma_totala_lei == suma_transport_lei + suma_produse_lei, "CIfrele costurilor platii nu coincid"

    def check_erorr_inputs_messages(self):
        erori_vizibile = 0
        list_of_errors = self.driver.find_elements(*DeliveryPageLocators.TEXTS_ERRORS)
        for i in range(len(list_of_errors)):
            if list_of_errors[i].is_displayed():
                erori_vizibile += 1
            else:
                pass
        print(erori_vizibile)
        print(list_of_errors)
        assert erori_vizibile < 1, f"{erori_vizibile} errors on the page"
