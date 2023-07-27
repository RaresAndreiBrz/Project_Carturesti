from selenium.webdriver.common.by import By

class DeliveryPageLocators:
    ACASA_OPTION = (By.XPATH, '//*[@id="w3"]/li[1]/a/div')
    LIBRARIE_OPTION = (By.XPATH, '//*[@id="w3"]/li[2]/a/div')
    LOCKER_OPTION = (By.XPATH, '//*[@id="w3"]/li[3]/a/div')
    TOWARDS_PAYMENT_BTN = (By.XPATH, '//*[@id="shipping-form"]/div[4]/div[2]/button')
    INDIVIDUAL_OPTION = (By.XPATH, '//*[@id="checkoutaddressform-is_company"]/label[1]/span')
    COMPANY_OPTION = (By.XPATH, '//*[@id="checkoutaddressform-is_company"]/label[2]/span')

    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="checkoutaddressform-firstname"]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="checkoutaddressform-lastname"]')
    PHONE_NR_INPUT = (By.XPATH, '//*[@id="checkoutaddressform-phone_number"]')
    COUNTRY_DROP_INPUT = (By.XPATH, '//*[@id="country-dropdown"]')
    COUNTRY_DROP_INPUT_ROMANIA = (By.XPATH, "//option[text()='Romania']")
    CITY_DROP_INPUT = (By.XPATH, '//*[@id="counties-dropdown"]')
    CITY_DROP_INPUT_BUCURESTI = (By.XPATH, '//*[@id="counties-dropdown"]/option[11]')
    TOWN_DROP_INPUT = (By.XPATH, '//*[@id="checkoutaddressform-id_city"]')
    TOWN_DROP_INPUT_SECTOR = (By.XPATH, '//*[@id="checkoutaddressform-id_city"]/option[4]')
    ADDRESS_TEXT_INPUT = (By.XPATH, '//*[@id="checkoutaddressform-address"]')
    ADD_ADDRESS = (By.XPATH, '//*[@id="shipping-form"]/div[2]/div[1]/div[3]/label')
    POSTAL_CODE_INPUT = (By.XPATH, '//*[@id="checkoutaddressform-zip_code"]')


    FREE_TRANSPORT_OPTION = (By.XPATH, '//*[@data-friendlyname="Transport Gratuit"]')
    BYCICLE_TRANSPORT_OPTION = (By.XPATH, '//*[@data-friendlyname="Livrare maine cu bicicleta"]')
    FAST_DELIVERY_TRANSPORT_OPTION = (By.XPATH, '//*[@data-friendlyname="Curier rapid"]')
    RETURNABLE_PACK_TRANSPORT_OPTION = (By.XPATH, '//*[@data-friendlyname="Ambalaj returnabil prin curier rapid"]')


    TOTAL_PRICE_OF_PRODUCTS_FROM_CART = (By.XPATH, '//*[@class="col-lg-3 col-md-3 col-sm-3 col-xs-3  p-0 cart-item-total"]')
    TOTAL_TRANSPORT_COST = (By.XPATH, '//html/body//div[1]/small[2]')
    TOTAL_AMOUNT_TO_PAY = (By.XPATH, '//*[@class="pull-right font-weight-bold"]')


    AFI_LOCATION_BUTTON = (By.XPATH, '//*[@id="physical-location-form"]/div[1]/div/div[3]/label/small')

    TEXTS_ERRORS = (By.XPATH, '//*[@class="help-block"]')

