import unittest
from selenium import webdriver

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.login_second_page import LoginSecondPage
from pages.summary_page import SummaryPage
from pages.delivery_page import DeliveryPage
from pages.home_page import HomePage
from pages.item_page import ItemPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.wishlist_page import WishlistPage


class BaseTests(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.homepage_object = HomePage(self.driver)
        self.loginsecondpage_object = LoginSecondPage(self.driver)
        self.productspage_object = ProductsPage(self.driver)
        self.itempage_object = ItemPage(self.driver)
        self.wishlistpage_object = WishlistPage(self.driver)
        self.wait_variable = BasePage(self.driver)
        self.checkoutpage_object = CheckoutPage(self.driver)
        self.deliverypage_object = DeliveryPage(self.driver)
        self.paymentpage_object = PaymentPage(self.driver)
        self.summarypage_object = SummaryPage(self.driver)
        # self.confirmationpage_object = ConfirmationPage(self.driver)
        self.driver.get('https://carturesti.ro/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
