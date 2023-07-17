import unittest
from selenium import webdriver

from Pages.assistance_page import AssistancePage
from Pages.base_page import BasePage
from Pages.checkout_page import CheckoutPage
from Pages.login_second_page import LoginSecondPage
from Pages.return_policy_page import ReturnPolicyPage
from Pages.summary_page import SummaryPage
from Pages.delivery_page import DeliveryPage
from Pages.home_page import HomePage
from Pages.item_page import ItemPage
from Pages.payment_page import PaymentPage
from Pages.products_page import ProductsPage
from Pages.wishlist_page import WishlistPage


class BaseTests(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

        self.homepage_object = HomePage(self.driver)
        self.loginsecondpage_object = LoginSecondPage(self.driver)
        self.assistancepage_object = AssistancePage(self.driver)
        self.productspage_object = ProductsPage(self.driver)
        self.itempage_object = ItemPage(self.driver)
        self.wishlistpage_object = WishlistPage(self.driver)
        self.wait_variable = BasePage(self.driver)
        self.checkoutpage_object = CheckoutPage(self.driver)
        self.deliverypage_object = DeliveryPage(self.driver)
        self.paymentpage_object = PaymentPage(self.driver)
        self.summarypage_object = SummaryPage(self.driver)
        self.returnpolicypage_object = ReturnPolicyPage(self.driver)
        self.driver.get('https://carturesti.ro/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
