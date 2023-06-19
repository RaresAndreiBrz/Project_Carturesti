from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    URL = 'https://carturesti.ro/'

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def wait_for_clickable_element(self, locator):
        wait_clickable = WebDriverWait(self.driver, 10)
        element = wait_clickable.until(EC.element_to_be_clickable(locator))
        return element

    def wait_for_displayed_element(self, locator):
        wait_displayed = WebDriverWait(self.driver, 10)
        element = wait_displayed.until(EC.presence_of_element_located(locator))
        return element

