import time

from behave import *


@then(u'I am adding an address')
def step_impl(context):
    context.deliverypage_object.click_on_add_address()
    time.sleep(1)


@then(u'I click on individual option')
def step_impl(context):
    context.deliverypage_object.click_on_persoana_fizica()
    time.sleep(1)


@then(u'I send valid inputs')
def step_impl(context):
    context.deliverypage_object.send_correct_inputs()
    time.sleep(1)


@then(u'I send invalid inputs')
def step_impl(context):
    context.deliverypage_object.send_correct_inputs()
    time.sleep(1)

    
@then(u'I go towards payment page')
def step_impl(context):
    time.sleep(5)
    context.deliverypage_object.establish_free_transport()
    time.sleep(5)
    context.deliverypage_object.go_to_payment_page()
    time.sleep(3)
    try:
        context.deliverypage_object.go_to_payment_page()
        time.sleep(3)
        context.deliverypage_object.establish_free_transport()
    except:
        pass
    try:
        context.deliverypage_object.go_to_payment_page()
        time.sleep(3)
        context.deliverypage_object.establish_free_transport()
    except:
        pass

    
    
@then(u'I should be still be on delivery page')
def step_impl(context):
    time.sleep(1)
    expected_url = "https://carturesti.ro/checkout/delivery"
    assert context.driver.current_url == expected_url, f"Expected {expected_url} instead of {context.driver.current_url}"

