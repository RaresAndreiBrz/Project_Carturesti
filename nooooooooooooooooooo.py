# #check out page locators not used
# PRICES_OF_INDIVIDUAL_ITEMS = (By.XPATH, '// *[ @data-label="Preț"]')  # LIST
# PRODUCTS_NAMES = (By.XPATH, '//*[@class="coloanaProdus kv-align-middle"]')
# PRODUCTS_SELECTED = (By.XPATH, '//*[@class="form-control" and @type="number"]')
#
#
# #ConfirmationPageLocators not used
# class ConfirmationPageLocators:
#     OFFERS_AND_DISCOUNTS = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[1]/md-checkbox/div[1]/div')
#     TOTAL_AMOUNT_TO_PAY_FOR_ORDER = (By.XPATH, '//*[@class="totalPrice pull-right"]')
#     TOTAL_AMOUNT_OF_PRODUCTS_TO_PAY = (By.XPATH, '//*[@data-label="Total"]')
#     TOTAL_AMOUNT_OF_TRANSPORT_TO_PAY = (By.XPATH, '//*[@class="shippingText"]')
#     ORDER_NUMBER = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/kbd')
#     LOCATION_OF_CONFIRMATION = (By.XPATH, '//*[@class="col-sm-6"][1]')
#     PARTIAL_MESSAGE_OF_CONFIRMATION_TEXT = "a fost înregistrată în sistem"
#
# #delivery page not used
#     BACK_TO_CART_BTN = (By.XPATH, '//*[@id="shipping-form"]/div[4]/div[1]/a/text()')
#     CITY_TO_SEND_PKG = (By.XPATH, '//*[@id="postis-delivery"]/div/div/div[2]//div[1]/div/span')
#     TOWN_TO_SEND_PKG = (By.XPATH, '//*[@id="postis-delivery"]/div/div/div[2]//div[1]/div[2]/div/span')
#     TOWN_SECTOR_6 = (By.XPATH, '//*[@id="postis-delivery"]/div/div/div[2]/div[2]/div/div[1]/div[2]/ul/li[6]')
#
#
# def click_on_livrare_acasa(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.ACASA_OPTION).click()
#
#
# def click_on_library_option(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.LIBRARIE_OPTION).click()
#
#
# def click_on_libraria_afi(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.AFI_LOCATION_BUTTON).click()
#
#
# def click_on_locker_option(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.LOCKER_OPTION).click()
#
#
# def click_on_libraria_afi(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.AFI_LOCATION_BUTTON).click()
#
#
# def click_on_locker_option(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.LOCKER_OPTION).click()
#
# def click_on_persoana_juridica(self):
#     self.wait_for_displayed_element(DeliveryPageLocators.COMPANY_OPTION).click()
#
# def stabileste_transport_gratuit(self):
#     try:
#         self.driver.find_element(*DeliveryPageLocators.FREE_TRANSPORT_OPTION).click()
#     except:
#         pass
#
#
# def stabileste_transport_curier_rapid(self):
#     try:
#         self.driver.find_element(*DeliveryPageLocators.FAST_DELIVERY_TRANSPORT_OPTION).click()
#     except:
#         pass
#
# def stabileste_transport_ambalaj_returnabil(self):
#     try:
#         self.driver.find_element(*DeliveryPageLocators.RETURNABLE_PACK_TRANSPORT_OPTION).click()
#     except:
#         pass
#
# def check_correct_amount_to_pay_from_delivery_page(self):
#     suma_produse = self.driver.find_elements(*DeliveryPageLocators.TOTAL_PRICE_OF_PRODUCTS_FROM_CART)
#     suma_produse_lei = 0
#     suma_transport = self.driver.find_elements(*DeliveryPageLocators.TOTAL_TRANSPORT_COST).text
#     suma_transport_lei = float(suma_transport.replace(',', '.').replace('RON', ''))
#     suma_totala = self.driver.find_element(*DeliveryPageLocators.TOTAL_AMOUNT_TO_PAY).text
#     suma_totala_lei = float(suma_totala.replace(',', '.').replace('RON', ''))
#     for pret in suma_produse:
#         suma_produse_lei += float(pret.text.replace(',', '.').replace('RON', ''))
#
#     assert suma_totala_lei == suma_transport_lei + suma_produse_lei, "CIfrele costurilor platii nu coincid"
#
#
# def check_erorr_inputs_messages(self):
#     erori_vizibile = 0
#     list_of_errors = self.driver.find_elements(*DeliveryPageLocators.TEXTS_ERRORS)
#     for i in range(len(list_of_errors)):
#         if list_of_errors[i].is_displayed():
#             erori_vizibile += 1
#         else:
#             pass
#     print(erori_vizibile)
#     print(list_of_errors)
#     assert erori_vizibile < 1, f"{erori_vizibile} errors on the page"
#
#     # Homepage not used
#     BTN_GOOGLE_LOGIN = (By.CLASS_NAME, "google auth-link")
#     BTN_FB_LOGIN = (By.CLASS_NAME, "facebook auth-link")
#
# #homepage not used
#
#     SIGNUP_SUCCESS_MSG_TEXT = "Inregistrarea a fost realizata cu succes. Am trimis un email de confirmare către adresa furnizata."
#     CART_EMPTY_MSSG = (By.CLASS_NAME, "checkout__empty ng-scope")
#     CART_EMPTY_MSSG_TEXT = "Nu aveți produse în coș."  # in html textul e urmat de spatii
#
# #asta e din item page not used
#     BTN_CONTACT = (By.PARTIAL_LINK_TEXT, "ontacteaz")
#
#     DETAILS_BOX = (By.XPATH, '//*[@class="row detailsContainer"]')
#
# #secon paage login not used stuff
#     PWD_OR_MAIL_ERROR = (By.XPATH, '//*[@id="login-form"]/div[2]/div[2]')
#
# #payment page not used
#     def select_onlineCard_option(self):
#         self.driver.find_element(*PaymentPageLocators.CARD_ONLINE_BTN).click()
#
#     def select_order_payment_option(self):
#         self.driver.find_element(*PaymentPageLocators.PAYMENT_ORDER_BTN).click()
#
#
# #summary page unused
#
#     def select_pack_items_separately(self):
#         self.driver.find_element(*ConfirmationPageLocators.PACK_GIFT_OPTION).click()
#         self.driver.find_element(*ConfirmationPageLocators.PACK_PRODUCTS_SEPARATELY).click()
#
# #wishlist unused
# def create_new_wishlist(self, wishlist_name):
#     self.driver.find_element(*WishlistPageLocators.INPUT_NAME_NEW_WISHLIST).send_keys(wishlist_name)
#     self.driver.find_element(*WishlistPageLocators.CREATE_NEW_WISHLIST_BTN).click()