import time

from behave import *


@then(u'I add it to cart as many times as I want')
def step_impl(context):
    context.itempage_object.multiply_clicks_on_add(2)
    time.sleep(2)

@then(u'I add it to cart multiple times')
def step_impl(context):
    context.itempage_object.multiply_clicks_on_add(11)
    time.sleep(13)

@then(u'I should see the box that contains the informations about the product')
def step_impl(context):
    context.itempage_object.check_details_displayed_box()

@then(u'I add it to my wishlist')
def step_impl(context):
    context.itempage_object.add_product_to_wishlist()