import time

from behave import *


@when(u'I click on products inventory')
def step_impl(context):
    context.homepage_object.click_on_products_inventory()

@then(u'I click on cart button')
def step_impl(context):
    context.productspage_object.click_on_cart_button()
    time.sleep(2)


@when(u'I put the cursor on music category')
def step_impl(context):
    context.homepage_object.put_cursor_on_music_category()


@then(u'I should see the list of categories of music section')
def step_impl(context):
    context.homepage_object.check_second_list_displayed()


@when(u'I put the cursor on disney category')
def step_impl(context):
    context.homepage_object.put_cursor_on_disney_category()


@then(u'I should see the list of categories of disney section')
def step_impl(context):
    context.homepage_object.check_second_list_displayed()

@then(u'I click on my account button')
def step_impl(context):
    context.homepage_object.click_on_my_account_btn()
@then(u'I click on wishlist button')
def step_impl(context):
    context.homepage_object.click_on_wishlist_btn()
@when(u'I cancel cookie section')
def step_impl(context):
    context.homepage_object.cancel_cookie()


@when(u'I go to policy section')
def step_impl(context):
    context.homepage_object.go_to_return_policy()

@when(u'I go to return policy')
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



@given("I click on login button")
def step_impl(context):
    context.homepage_object.click_login_button()
    time.sleep(1)


@given("I select existing user")
def step_impl(context):
    context.homepage_object.select_existing_user()
    time.sleep(1)


@given("I enter a valid mail")
def step_impl(context):
    context.homepage_object.complete_mail_for_login()


@given("I enter valid credentials")
def step_impl(context):
    context.loginsecondpage_object.send_correct_mail_correct_pwd()


@given("I enter a valid password")
def step_impl(context):
    context.homepage_object.complete_pwd_for_login()


@given("I enter an invalid password")
def step_impl(context):
    context.homepage_object.complete_wrong_pwd_for_login()


@given("I enter an invalid mail")
def step_impl(context):
    context.homepage_object.complete_wrong_mail_for_login()


@given("I enter no password")
def step_impl(context):
    pass


@given("I enter no mail")
def step_impl(context):
    pass


@given("I click on authentication button")
def step_impl(context):
    context.homepage_object.click_on_auth_button()
    time.sleep(1)


@then("I should be able to see that i am logged in")
def step_impl(context):
    context.homepage_object.check_signing_in_succesfully()


@then("I should be able to see an error message")
def step_impl(context):
    context.homepage_object.check_wrong_pwd_mail_mssg()


@then("I should be redirected to login form page")
def step_impl(context):
    expected_url = 'https://carturesti.ro/site/login'
    initial_url = 'https://carturesti.ro/'
    assert initial_url != context.driver.current_url, f'Expected {expected_url} instead of f{initial_url}'


@given("I send invalid credentials on the login form")
def step_impl(context):
    context.loginsecondpage_object.send_wrong_mail_wrong_pwd()


@then("I should be on the same page")
def step_impl(context):
    expected_url = 'https://carturesti.ro/site/login'
    initial_url = 'https://carturesti.ro/site/login'
    assert initial_url == context.driver.current_url, f'Expected {expected_url} instead of f{context.driver.current_url}'


@given(u'I click on authentication button from LoginForm')
def step_impl(context):
    context.loginsecondpage_object.click_on_auth_btn()
    time.sleep(1)


@given(u'I enter invalid mail and valid password')
def step_impl(context):
    context.loginsecondpage_object.send_wrong_mail_correct_pwd()


@given(u'I enter valid mail and invalid password')
def step_impl(context):
    context.loginsecondpage_object.send_correct_mail_wrong_pwd()


@given(u'I am logged in')
def step_impl(context):
    context.homepage_object.click_login_button()
    context.homepage_object.select_existing_user()
    context.homepage_object.complete_mail_for_login()
    context.homepage_object.complete_pwd_for_login()
    context.homepage_object.click_on_auth_button()

@given(u'I search an invalid text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar("bazzzzzzz")
    context.homepage_object.submit_search_text()



@given(u'I search a random text on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('portocala')
    context.homepage_object.submit_search_text()
    time.sleep(1)

@given(u'I search a product on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('george')
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

@given(u'I search a new word on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('masca')
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


@when(u'I select descending alphabetical order')
def step_impl(context):
    context.productspage_object.sort_alphabet_desc()
    time.sleep(1)


@when(u'I random select a number of items to be shown')
def step_impl(context):
    context.productspage_object.random_sort_of_items_number_on_page()


@when(u'I select ascending discount order')
def step_impl(context):
    context.productspage_object.sort_discount_asc()
    time.sleep(1)


@then(u'I should see that the product do not exists')
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


@then(u'I should see available products sorted alphabetical descending order correctly')
def step_impl(context):
    context.productspage_object.check_sort_alphabetic_descending()


@then(u'I should see available products sorted alphabetical ascending order correctly')
def step_impl(context):
    time.sleep(1)
    context.productspage_object.check_sort_alphabetic_ascending()


@then(u'I should see more than half products shown with this text included in name')
def step_impl(context):
    time.sleep(1)
    context.productspage_object.check_name_relevance_products_received('portocala')



@then(u'I go back')
def step_impl(context):
    context.driver.back()



@given(u'I search a word on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('NAPOLEON')
    context.homepage_object.submit_search_text()

@given(u'I search a random word on site')
def step_impl(context):
    context.homepage_object.send_text_to_search_bar('albastru')
    context.homepage_object.submit_search_text()
@when(u'I select descending discount order')
def step_impl(context):
    context.productspage_object.sort_discount_desc()
    time.sleep(1)


@when(u'I select ascending alphabetical order')
def step_impl(context):
    context.productspage_object.sort_alphabet_asc()
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
