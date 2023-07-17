import time

from behave import *


@then(u'I add it to cart as many times i want')
def step_impl(context):
    context.itempage_object.multiply_clicks_on_add(1)


@then(u'I add it to cart multiple times')
def step_impl(context):
    context.itempage_object.multiply_clicks_on_add(11)
