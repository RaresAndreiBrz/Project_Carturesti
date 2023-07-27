
import time

from behave import *

@then(u'I click on first product seen on page')
def step_impl(context):
    context.productspage_object.click_on_first_item()


@then(u'I should see the added items number being equivalent with the number from logo cart')
def step_impl(context):
    context.productspage_object.check_items_number_on_cart()

@then(u'I go to checkout page')
def step_impl(context):
    context.productspage_object.go_to_checkout_page()

@then(u'I click on second product seen on page')
def step_impl(context):
    context.productspage_object.click_on_second_item()



@then(u'I remove an item from cart')
def step_impl(context):
    context.productspage_object.click_remove_in_cart()


@then(u'I should see the correct price of my items')
def step_impl(context):
    context.productspage_object.check_price_in_cart()

