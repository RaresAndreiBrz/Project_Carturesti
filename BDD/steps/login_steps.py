import time

from behave import *


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
