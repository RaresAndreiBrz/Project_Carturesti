import time

from behave import *

@then(u'I check the presence of my product in wishlist')
def step_impl(context):
    context.wishlistpage_object.check_presence_of_products_in_wishlist()

@then(u'I remove it from wishlist')
def step_impl(context):
    context.wishlistpage_object.remove_products_from_wishlists()