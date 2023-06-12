import time
from base_test import BaseTests


class Tests(BaseTests):
  
    # def test_signup(self):
    #     self.homepage_object.click_login_button()
    #     self.homepage_object.select_new_user()
    #     self.homepage_object.complete_mail_for_signup()
    #     self.homepage_object.complete_pwd_for_signup()
    #     self.homepage_object.click_recaptcha_box()
    #     self.homepage_object.click_on_auth_button()
    #     self.homepage_object.check_sign_up_succesfully()

    def test_sign_in(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        self.homepage_object.check_signing_in_succesfully()

    def test_sign_in_no_pwd(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.click_on_auth_button()
        self.homepage_object.check_wrong_pwd_mail_mssg()

    def test_sign_in_no_mail(self):
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        self.homepage_object.check_wrong_pwd_mail_mssg()

    def test_sign_in_wrong_pwd(self):
        current_url_before_signing_in = self.driver.current_url
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_mail_for_login()
        self.homepage_object.complete_wrong_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        time.sleep(1.5)
        assert current_url_before_signing_in != self.driver.current_url, f'apare asta{self.driver.current_url}'

    def test_sign_in_wrong_mail(self):
        current_url_before_signing_in = self.driver.current_url
        self.homepage_object.click_login_button()
        self.homepage_object.select_existing_user()
        self.homepage_object.complete_wrong_mail_for_login()
        self.homepage_object.complete_pwd_for_login()
        self.homepage_object.click_on_auth_button()
        time.sleep(1.5)
        assert current_url_before_signing_in != self.driver.current_url, f'Apare {current_url_before_signing_in} \
                                                                in loc de "https://carturesti.ro/site/login" '

    def test_sort_price_ascending(self):
        self.homepage_object.send_text_to_search_bar('jordan peterson')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_price_asc()
        self.productspage_object.check_sort_prices_ascending()

    def test_sort_price_descending(self):
        self.homepage_object.send_text_to_search_bar('jordan peterson')
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_price_desc()
        self.productspage_object.check_sort_prices_descending()


    def test_sort_alfabetic_asc_produse_in_stoc(self):
        self.homepage_object.send_text_to_search_bar('portocala')
        self.homepage_object.submit_search_text()
        self.productspage_object.sort_in_stoc_items()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_alfabet_asc()
        self.productspage_object.check_sort_alfabetic_ascending()

    def test_sort_alfabetic_desc_produse_in_stoc(self):
        self.homepage_object.send_text_to_search_bar('portocala')
        self.homepage_object.submit_search_text()
        self.productspage_object.sort_in_stoc_items()
        self.productspage_object.click_on_sort_button()
        self.productspage_object.sort_alfabet_desc()
        self.productspage_object.check_sort_alfabetic_descending()

    def test_elements_shown_on_page(self, text_to_check='portocala'):
        self.driver.text_to_check = text_to_check
        self.homepage_object.send_text_to_search_bar(text_to_check)
        self.homepage_object.submit_search_text()
        self.productspage_object.click_on_sort_itemsNr_button()
        self.productspage_object.random_sort_of_items_number_on_page()
        self.productspage_object.check_items_number_on_page()


    def test_correct_items_number_in_cart(self):
        self.homepage_object.login_procedure()
        self.homepage_object.send_text_to_search_bar("jordan peterson")
        self.homepage_object.submit_search_text()
        self.productspage_object.add_book_JP()
        self.productspage_object.back()
        self.productspage_object.add_book_JP_2()
        self.productspage_object.back()
        self.productspage_object.check_items_number_on_cart()

    def test_only_in_stoc_button_active(self):
        self.homepage_object.send_text_to_search_bar('portocala')
        self.homepage_object.submit_search_text()
        self.productspage_object.sort_in_stoc_items()
        self.productspage_object.check_disponibility_sort_buttons()
