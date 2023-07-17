from selenium.webdriver.common.by import By


class ConfirmationPageLocators:
    PACK_GIFT_OPTION = (By.XPATH, '//*[@id="finalize-checkout-form"]//div/div[1]/div[2]/div[1]/label/span')
    PACK_ALL_PRODUCTS = (By.XPATH, '//*[@id="dynamicmodel-giftwrap_together"]/label[1]/span')
    PACK_PRODUCTS_SEPARATELY = (By.XPATH, '//*[@id="dynamicmodel-giftwrap_together"]/label[2]/span')
    FINISH_ORDER = (By.XPATH, '//*[@id="finalize-checkout-button"]')

    OBSERVATIONS_INPUT = (By.XPATH, '//*[@id="checkoutorder-observation"]')

