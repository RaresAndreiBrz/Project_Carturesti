import time

from behave import *


@given(u'I search a random text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('portocala')
    context.homepage_object.submit_search_text()
    time.sleep(1)


@given(u'I search another random text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('matematica')
    context.homepage_object.submit_search_text()
    time.sleep(1)


@given(u'I search a specific text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('bazz')
    context.homepage_object.submit_search_text()
    time.sleep(1)


@when(u'I select in stoc products')
def step_impl(context):
    context.productspage_object.sort_in_stoc_items()
    time.sleep(1)


@when(u'I click on second sorting button')
def step_impl(context):
    context.productspage_object.click_on_sort_itemsNr_button()
    time.sleep(1)


@when(u'I select descending alfabetical order')
def step_impl(context):
    context.productspage_object.sort_alfabet_desc()
    time.sleep(1)


@when(u'I random select a number of items to be shown')
def step_impl(context):
    context.productspage_object.random_sort_of_items_number_on_page()


@when(u'I select ascending discount order')
def step_impl(context):
    context.productspage_object.sort_discount_asc()
    time.sleep(1)


@given(u'I search an invalid text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar("bazzzzzzz")
    context.homepage_object.submit_search_text()


@then(u'I should see that the product do not exist')
def step_impl(context):
    context.homepage_object.check_error_of_missing_product()


@then(u'I should see only In Stoc button active')
def step_impl(context):
    context.productspage_object.check_disponibility_sort_buttons()


@given(u'I search a valid text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('jordan peterson')
    context.homepage_object.submit_search_text()


@when(u'I click on sorting button')
def step_impl(context):
    context.productspage_object.click_on_sort_button()


@when(u'I select ascending order of price')
def step_impl(context):
    context.productspage_object.sort_price_asc()


@then(u'I should see the products sorted descending correctly')
def step_impl(context):
    context.productspage_object.check_sort_prices_descending()


@when(u'I select descending order of price')
def step_impl(context):
    context.productspage_object.sort_price_desc()


@then(u'I should see more than half products shown from the author')
def step_impl(context):
    time.sleep(1)
    context.productspage_object.check_author_relevance_products_received('jordan b. peterson')


@then(u'I should see products sorted by discount descending order correctly')
def step_impl(context):
    context.productspage_object.check_sort_discount_desc()


@then(u'I should see available products sorted alfabetical descending order correctly')
def step_impl(context):
    context.productspage_object.check_sort_alfabetic_descending()


@then(u'I should see available products sorted alfabetical ascending order correctly')
def step_impl(context):
    time.sleep(1)
    context.productspage_object.check_sort_alfabetic_ascending()


@then(u'I should see more than half products shown with this text included in name')
def step_impl(context):
    time.sleep(1)
    context.productspage_object.check_name_relevance_products_received('portocala')


@then(u'I should see the added items number being equivalent with the number from logo cart')
def step_impl(context):
    context.productspage_object.check_items_number_on_cart()


@given(u'I search a word on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('NAPOLEON')
    context.homepage_object.submit_search_text()


@when(u'I select descending discount order')
def step_impl(context):
    context.productspage_object.sort_discount_desc()
    time.sleep(1)


@when(u'I select ascending alfabetical order')
def step_impl(context):
    context.productspage_object.sort_alfabet_asc()
    time.sleep(1)


@then(u'I should see the products sorted ascending correctly')
def step_impl(context):
    context.productspage_object.check_sort_prices_ascending()


@then(u'I should see no more items than the number randomly selected')
def step_impl(context):
    context.productspage_object.check_items_number_on_page()


@then(u'I should see products sorted by discount ascending order correctly')
def step_impl(context):
    context.productspage_object.check_sort_discount_asc()
