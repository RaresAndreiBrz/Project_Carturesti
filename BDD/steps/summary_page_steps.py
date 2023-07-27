import time

from behave import *



@then(u'I select items as gifts')
def step_impl(context):
    context.summarypage_object.select_gift_items()
    time.sleep(5)


@then(u'I fill the observations box')
def step_impl(context):
    context.summarypage_object.complete_observations()
    time.sleep(5)

@then(u'I finish the purchase')
def step_impl(context):
    context.summarypage_object.finish_order()
    time.sleep(5)