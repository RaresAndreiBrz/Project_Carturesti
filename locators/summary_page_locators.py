from selenium.webdriver.common.by import By


class ConfirmationPageLocators:
    PACK_GIFT_OPTION = (By.XPATH, "//input[@name='CheckoutOrder[option_giftwrap]'])[2]")
    PACK_ALL_PRODUCTS = (By.XPATH, '//*[@id="dynamicmodel-giftwrap_together"]/label[1]/span')
    PACK_PRODUCTS_SEPARATELY = (By.XPATH, '//*[@id="dynamicmodel-giftwrap_together"]/label[2]/span')
    ADD_NEWSLETTER = (By.XPATH, '//*[@id="finalize-checkout-form"]/div[2]/div[1]/div/div/div[1]/div[2]/div[3]/label/span')
    FINISH_ORDER = (By.XPATH, '//*[@id="finalize-checkout-button"]')

    OBSERVATIONS_INPUT = (By.XPATH, '//*[@id="checkoutorder-observation"]')

