import time

from behave import *



@then(u'I select to pay with cash')
def step_impl(context):
    context.paymentpage_object.select_cash_on_receiving_option()

@then(u'I go to summary page')
def step_impl(context):
    context.paymentpage_object.go_to_summary_page()