import unittest
from selenium import webdriver

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.item_page import ItemPage
from pages.products_page import ProductsPage


class BaseTests(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.homepage_object = HomePage(self.driver)
        self.productspage_object = ProductsPage(self.driver)
        self.itempage_object = ItemPage(self.driver)
        self.wait_variable = BasePage(self.driver)
        self.checkoutpage_object = CheckoutPage(self.driver)
        self.driver.get('https://carturesti.ro/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
