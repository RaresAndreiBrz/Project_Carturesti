import time

from behave import *

@then(u'I should be able to see the tile')
def step_impl(context):
    context.returnpolicypage_object.check_title_is_displayed()


@then(u'I should be able to see the text')
def step_impl(context):
    context.returnpolicypage_object.check_text_is_displayed()