import time

from behave import *


@when(u'I click on products inventory')
def step_impl(context):
    context.homepage_object.click_on_products_inventory()


@then(u'I remove an item from cart')
def step_impl(context):
    context.productspage_object.click_remove_in_cart()


@then(u'I should see the correct price of my items')
def step_impl(context):
    context.productspage_object.check_price_in_cart()


@then(u'I click on cart button')
def step_impl(context):
    context.productspage_object.click_on_cart_button()
    time.sleep(2)


@when(u'I put the cursor on music category')
def step_impl(context):
    context.homepage_object.put_cursor_on_music_category()


@then(u'I click on first product seen on page')
def step_impl(context):
    context.productspage_object.click_on_first_item()


@then(u'I should see the list of categories of music section')
def step_impl(context):
    context.homepage_object.check_second_list_displayed()


@when(u'I put the cursor on disney category')
def step_impl(context):
    context.homepage_object.put_cursor_on_disney_category()


@then(u'I should see the list of categories of disney section')
def step_impl(context):
    context.homepage_object.check_second_list_displayed()


@when(u'I cancel cookie section')
def step_impl(context):
    context.homepage_object.cancel_cookie()


@when(u'I go to policy section')
def step_impl(context):
    context.homepage_object.go_to_return_policy()


@then(u'I should see text displayed regarding policy')
def step_impl(context):
    context.returnpolicypage_object.check_title_is_displayed()
    context.returnpolicypage_object.check_text_is_displayed()


@then(u'I should see buttons displayed and their informations displayed')
def step_impl(context):
    context.assistancepage_object.check_buttons_nr_equal_with_text_boxes()


@when(u'I go to assistance section')
def step_impl(context):
    context.homepage_object.go_to_assistance_page()
