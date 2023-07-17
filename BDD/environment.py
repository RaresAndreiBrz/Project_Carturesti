from selenium import webdriver

from Pages.assistance_page import AssistancePage
from Pages.checkout_page import CheckoutPage
from Pages.delivery_page import DeliveryPage
from Pages.home_page import HomePage
from Pages.item_page import ItemPage
from Pages.login_second_page import LoginSecondPage
from Pages.payment_page import PaymentPage
from Pages.products_page import ProductsPage
from Pages.return_policy_page import ReturnPolicyPage
from Pages.summary_page import SummaryPage
from Pages.wishlist_page import WishlistPage



def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get('https://carturesti.ro/')
    context.driver.maximize_window()
    context.homepage_object = HomePage(context.driver)
    context.loginsecondpage_object = LoginSecondPage(context.driver)
    context.assistancepage_object = AssistancePage(context.driver)
    context.productspage_object = ProductsPage(context.driver)
    context.itempage_object = ItemPage(context.driver)
    context.wishlistpage_object = WishlistPage(context.driver)
    context.checkoutpage_object = CheckoutPage(context.driver)
    context.deliverypage_object = DeliveryPage(context.driver)
    context.paymentpage_object = PaymentPage(context.driver)
    context.summarypage_object = SummaryPage(context.driver)
    context.returnpolicypage_object = ReturnPolicyPage(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()