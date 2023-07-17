from selenium.webdriver.common.by import By

class ReturnPolicyPageLocators:

    TITLE_OF_POLICY = (By.XPATH, '//*[@class="cartu-section-title pageTitle"]')
    TEXT_OF_POLICY = (By.XPATH, '//*[@class="descriere"]')