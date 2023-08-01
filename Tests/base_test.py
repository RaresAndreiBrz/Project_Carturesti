import unittest
from pages.assistance_page import AssistancePage
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.delivery_page import DeliveryPage
from pages.home_page import HomePage
from pages.item_page import ItemPage
from pages.login_second_page import LoginSecondPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.return_policy_page import ReturnPolicyPage
from pages.summary_page import SummaryPage
from pages.wishlist_page import WishlistPage


class BaseTests(BasePage,unittest.TestCase):

    def setUp(self) -> None:
        # self.driver = webdriver.Chrome()
        self.homepage_object = HomePage()
        self.loginsecondpage_object = LoginSecondPage()
        self.assistancepage_object = AssistancePage()
        self.productspage_object = ProductsPage()
        self.itempage_object = ItemPage()
        self.wishlistpage_object = WishlistPage()
        self.wait_variable = BasePage()
        self.checkoutpage_object = CheckoutPage()
        self.deliverypage_object = DeliveryPage()
        self.paymentpage_object = PaymentPage()
        self.summarypage_object = SummaryPage()
        self.returnpolicypage_object = ReturnPolicyPage()
        self.driver.get('https://carturesti.ro/')
        self.driver.maximize_window()
        self.driver.set_script_timeout(50)

    def tearDown(self):
        self.driver.quit()


    def back(self):
        self.driver.back()
