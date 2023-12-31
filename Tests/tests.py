import time
import unittest

from base_test import BaseTests

class Tests(BaseTests):

#recaptcha requirements
    # def test_signup(self):
    #     self.homepage_object.click_login_button()
    #     self.homepage_object.select_new_user()
    #     self.homepage_object.complete_mail_for_signup()
    #     self.homepage_object.complete_pwd_for_signup()
    #     self.homepage_object.click_recaptcha_box()
    #     self.homepage_object.click_on_auth_button()
    #     self.homepage_object.check_sign_up_succesfully()

#slide bar problems
# def test_review_an_item(self):
#     self.homepage_object.send_text_to_search_bar("laurentiu")
#     self.homepage_object.submit_search_text()
#     self.productspage_object.click_on_first_item()
#     self.itempage_object.review_the_item(9)

    @unittest.skip
    def test_sign_in(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        self.homepage_object.check_signing_in_succesfully()

    @unittest.skip
    def test_sign_in_without_pwd(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.click_on_auth_button()
        self.homepage_object.check_wrong_pwd_mail_mssg()

    @unittest.skip
    def test_sign_in_without_mail(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        self.homepage_object.check_wrong_pwd_mail_mssg()

    @unittest.skip
    def test_sign_in_with_invalid_pwd(self):
        current_url_before_signing_in = self.driver.current_url
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_wrong_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        expected_url = 'https://carturesti.ro/site/login'
        assert current_url_before_signing_in != self.driver.current_url, f'Expected {expected_url} instead of ' \
                                                                         f'{self.driver.current_url}'

    @unittest.skip
    def test_sign_in_with_invalid_mail(self):
        url_before_signing_in = self.driver.current_url
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_wrong_mail_for_login()
        self.homepage_object.complete_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        expected_url = 'https://carturesti.ro/site/login'
        assert url_before_signing_in != self.driver.current_url, f'Expected{expected_url} instead of ' \
                                                                 f'{url_before_signing_in}'

    @unittest.skip
    def test_second_loginPage_with_invalid_credentials(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_wrong_mail_for_login()
        self.homepage_object.complete_wrong_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        this_url = self.driver.current_url
        self.loginsecondpage_object.send_wrong_mail_wrong_pwd()
        self.loginsecondpage_object.click_on_auth_btn()
        assert this_url == self.driver.current_url, f"Url changed. Expected {this_url} and got " \
                                                    f"{self.driver.current_url}"

    @unittest.skip
    def test_second_loginPage_with_invalid_mail_and_valid_pwd(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_wrong_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        this_url = self.driver.current_url
        self.loginsecondpage_object.send_wrong_mail_correct_pwd()
        self.loginsecondpage_object.click_on_auth_btn()
        assert this_url == self.driver.current_url, f"Url changed. Expected {this_url} and got " \
                                                    f"{self.driver.current_url}"

    @unittest.skip
    def test_second_loginPage_with_valid_mail_and_invalid_pwd(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_wrong_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        this_url = self.driver.current_url
        self.loginsecondpage_object.send_correct_mail_wrong_pwd()
        self.loginsecondpage_object.click_on_auth_btn()
        assert this_url == self.driver.current_url, f"Url changed. Expected {this_url} and got " \
                                                    f"{self.driver.current_url}"

    @unittest.skip
    def test_second_loginPage_with_valid_credentials(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_wrong_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        this_url = self.driver.current_url
        self.loginsecondpage_object.send_correct_mail_correct_pwd()
        self.loginsecondpage_object.click_on_auth_btn()
        time.sleep(1)
        assert this_url != self.driver.current_url, f"Url changed. Expected 'https://carturesti.ro/' and got" \
                                                    f" {self.driver.current_url}"

    @unittest.skip
    def test_unavailable_product(self):
        self.homepage_object.send_text_to_search_bar("bazzzzzzz")
        initial_url = self.driver.current_url
        self.homepage_object.submit_search_text()
        expected_url = 'https://carturesti.ro/product/search/bazzzzzzz'
        self.homepage_object.check_error_of_missing_product()
        assert initial_url != expected_url, f"Expected {expected_url} and received {self.driver.current_url}"

    @unittest.skip
    def test_of_sorting_price_ascending_order(self):
        self.homepage_object.send_text_to_search_bar('jordan peterson')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_price_asc()
        self.productspage_object.check_sort_prices_ascending()

    @unittest.skip
    def test_of_sorting_price_descending_order(self):
        self.homepage_object.send_text_to_search_bar('jordan peterson')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_price_desc()
        self.productspage_object.check_sort_prices_descending()

    @unittest.skip
    def test_sort_alphabetic_ascending_order_products_in_stoc(self):
        self.homepage_object.send_text_to_search_bar('portocala')
        self.homepage_object.submit_search_text()
        self.productspage_object.sort_in_stoc_items()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_alphabet_asc()
        self.productspage_object.check_sort_alphabetic_ascending()

    @unittest.skip
    def test_sort_alphabetic_descending_order_products_in_stoc(self):
        self.homepage_object.send_text_to_search_bar('portocala')
        self.homepage_object.submit_search_text()
        self.productspage_object.sort_in_stoc_items()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_alphabet_desc()
        self.productspage_object.check_sort_alphabetic_descending()

    @unittest.skip
    def test_sort_discount_desc_products(self):
        self.homepage_object.send_text_to_search_bar('matematica')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_discount_desc()
        self.productspage_object.check_sort_discount_desc()

    @unittest.skip
    def test_sort_discount_asc_products(self):
        self.homepage_object.send_text_to_search_bar('matematica')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_discount_asc()
        self.productspage_object.check_sort_discount_asc()

    @unittest.skip
    def test_elements_shown_on_page(self, text_to_check='bazz'):
        self.driver.text_to_check = text_to_check
        self.homepage_object.send_text_to_search_bar(text_to_check)
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_items_number_button()
        self.productspage_object.random_sort_of_items_number_on_page()
        self.productspage_object.check_items_number_on_page()

    @unittest.skip
    def test_correct_items_number_in_cart(self):
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar("jordan peterson")
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(1)
        self.productspage_object.check_items_number_on_cart()

    @unittest.skip
    def test_only_in_stoc_button_active(self):
        self.homepage_object.send_text_to_search_bar('portocala')
        time.sleep(4)
        self.homepage_object.submit_search_text()
        time.sleep(4)
        self.productspage_object.sort_in_stoc_items()
        time.sleep(10)
        self.productspage_object.check_disponibility_sort_buttons()


    @unittest.skip
    def test_relevance_products_received_by_author(self):       # relevant means over 50 % with correct authors
        self.homepage_object.send_text_to_search_bar('jordan b. peterson')
        self.homepage_object.submit_search_text()
        self.productspage_object.check_author_relevance_products_received('jordan b. peterson')


    @unittest.skip
    def test_relevance_products_received_by_name(self):   # relevant means over 50 % with correct names
        self.homepage_object.send_text_to_search_bar('portocala')
        self.homepage_object.submit_search_text()
        self.productspage_object.check_name_relevance_products_received('portocala')

    @unittest.skip
    def test_limit_number_of_items_in_cart(self):    # 10 is the limit of products in cart
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar('NAPOLEON')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(11)
        self.productspage_object.check_items_number_on_cart()

    @unittest.skip
    def test_in_cart_removal_of_items(self):
        self.homepage_object.send_text_to_search_bar('NAPOLEON')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(1)
        self.driver.back()
        self.productspage_object.click_on_second_item()
        self.itempage_object.multiply_clicks_on_add(2)
        self.productspage_object.click_on_cart_button()
        time.sleep(4)
        self.productspage_object.click_remove_in_cart()
        # time.sleep()
        self.productspage_object.check_items_number_on_cart()

    @unittest.skip
    def test_final_price_displayed_in_cart_button(self):
        self.homepage_object.send_text_to_search_bar('NAPOLEON')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(1)
        self.driver.back()
        self.productspage_object.click_on_second_item()
        self.itempage_object.multiply_clicks_on_add(2)
        self.productspage_object.click_on_cart_button()
        self.productspage_object.check_price_in_cart()

    @unittest.skip
    def test_details_displayed_on_item_page(self):
        self.homepage_object.send_text_to_search_bar("george")
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.check_details_displayed_box()

    @unittest.skip
    def test_add_product_to_wishlist(self):
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar("albastru")
        self.homepage_object.submit_search_text()
        self.homepage_object.cancel_cookie()
        self.productspage_object.click_on_first_item()
        self.itempage_object.add_product_to_wishlist()
        self.homepage_object.click_on_my_account_btn()
        self.homepage_object.click_on_wishlist_btn()
        self.wishlistpage_object.check_presence_of_products_in_wishlist()
        self.wishlistpage_object.remove_products_from_wishlists()

    @unittest.skip
    def test_remove_button_from_checkout_page(self):
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar("masca")
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(3)
        self.driver.back()
        self.productspage_object.click_on_second_item()
        self.itempage_object.multiply_clicks_on_add(1)
        self.productspage_object.click_on_cart_button()
        self.productspage_object.go_to_checkout_page()
        self.checkoutpage_object.check_amount_to_pay_for_all_products()
        self.checkoutpage_object.random_remove()
        self.checkoutpage_object.check_amount_to_pay_for_all_products()

    @unittest.skip
    def test_wrong_info_delivery_inputs1(self):
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar("albastru")
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(2)
        self.productspage_object.click_on_cart_button()
        self.productspage_object.go_to_checkout_page()
        self.homepage_object.cancel_cookie()
        self.checkoutpage_object.go_to_delivery_page()
        self.deliverypage_object.click_on_add_address()
        self.deliverypage_object.click_on_persoana_fizica()
        self.current_url = self.driver.current_url
        self.deliverypage_object.send_wrong_inputs()
        assert self.current_url == self.driver.current_url, f"Expected {self.current_url} " \
                                                            f"instead of {self.driver.current_url}"

    def test_finishing_an_order_at_address(self):
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar("matematica")
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_first_item()
        self.itempage_object.multiply_clicks_on_add(2)
        self.productspage_object.click_on_cart_button()
        self.productspage_object.go_to_checkout_page()
        self.homepage_object.cancel_cookie()
        self.checkoutpage_object.go_to_delivery_page()
        time.sleep(1)
        self.deliverypage_object.click_on_add_address()
        self.deliverypage_object.click_on_persoana_fizica()
        self.deliverypage_object.send_correct_inputs()
        time.sleep(5)
        self.deliverypage_object.go_to_payment_page()
        time.sleep(5)
        self.paymentpage_object.select_cash_on_receiving_option()
        self.paymentpage_object.go_to_summary_page()
        time.sleep(2)
        self.summarypage_object.select_gift_items()
        time.sleep(5)
        self.summarypage_object.complete_observations()
        time.sleep(15)
        self.summarypage_object.finish_order()
        time.sleep(10)


    @unittest.skip
    def test_return_policy_is_displayed(self):
        self.homepage_object.cancel_cookie()
        self.homepage_object.go_to_return_policy()
        self.returnpolicypage_object.check_title_is_displayed()
        self.returnpolicypage_object.check_text_is_displayed()

    @unittest.skip
    def test_items_of_music_category(self):
        self.homepage_object.cancel_cookie()
        self.homepage_object.click_on_products_inventory()
        self.homepage_object.put_cursor_on_music_category()
        self.homepage_object.check_second_list_displayed()

    @unittest.skip
    def test_items_of_disney_category(self):
        self.homepage_object.cancel_cookie()
        self.homepage_object.click_on_products_inventory()
        self.homepage_object.put_cursor_on_disney_category()
        self.homepage_object.check_second_list_displayed()

    @unittest.skip
    def test_buttons_informations_check_display(self):
        self.homepage_object.cancel_cookie()
        self.homepage_object.go_to_assistance_page()
        self.assistancepage_object.check_buttons_nr_equal_with_text_boxes()
