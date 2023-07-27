import time

from behave import *



@when(u'I random remove a product from list')
def step_impl(context):
    context.checkoutpage_object.random_remove()
    time.sleep(1)

@when(u'I go to delivery page')
def step_impl(context):
    context.checkoutpage_object.go_to_delivery_page()
    time.sleep(1)

@then(u'I check the price of my products')
def step_impl(context):
    context.checkoutpage_object.check_amount_to_pay_for_all_products()


@then(u'I should have the total price of my products correctly displayed')
def step_impl(context):
    context.checkoutpage_object.check_amount_to_pay_for_all_products()