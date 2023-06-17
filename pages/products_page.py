import time
import random

from selenium.webdriver.common.by import By

from locators.home_page_locators import HomePageLocators
from locators.item_page_locators import ItemPageLocators
from locators.products_page_locators import ProductsPageLocators
from pages.base_page import BasePage


class ProductsPage(BasePage):

    def click_on_sort_button(self):
        time.sleep(1)
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT1)
        button.click()

    def sort_price_asc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_PRICE_ASC)
        button.click()

    def sort_price_desc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_PRICE_DESC)
        button.click()

    def sort_alfabet_asc(self):
        self.driver.find_element(*ProductsPageLocators.BTN_SORT_ALFAB_ASC).click()

    def sort_alfabet_desc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_ALFAB_DESC)
        button.click()

    def sort_discount_asc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_DISCOUNT_ASC)
        button.click()
        time.sleep(1)

    def sort_discount_desc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_DISCOUNT_DESC)
        button.click()
        time.sleep(1)

    def click_on_sort_itemsNr_button(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT2_PRODUCT_TO_DISPLAY)
        button.click()

    def select_30_items_onPage(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_30_PRODUCTS_TO_DISPLAY)
        button.click()

    def select_60_items_onPage(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_60_PRODUCTS_TO_DISPLAY)
        button.click()

    def select_90_items_onPage(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_90_PRODUCTS_TO_DISPLAY)
        button.click()

    def random_sort_of_items_number_on_page(self):
        select_items_random = [self.select_30_items_onPage, self.select_60_items_onPage, self.select_90_items_onPage]
        item_chosen_randomly = random.choice(select_items_random)
        item_chosen_randomly()

    def check_sort_prices_ascending(self):
        time.sleep(1)
        self.preturi_asc = []
        for pret in self.driver.find_elements(*ProductsPageLocators.PRODUCTS_PRICES):
            self.preturi_asc.append(int(float(pret.text)))
        self.preturi_asc_check = all(
            self.preturi_asc[i] <= self.preturi_asc[i + 1] for i in range(len(self.preturi_asc) - 1))
        assert self.preturi_asc_check == True, 'Prices ascending order wrong sorted.'

    def check_sort_prices_descending(self):
        time.sleep(1)
        self.preturi_desc = []
        for pret in self.driver.find_elements(*ProductsPageLocators.PRODUCTS_PRICES):
            self.preturi_desc.append(int(float(pret.text)))
        self.preturi_desc_check = all(
            self.preturi_desc[i] >= self.preturi_desc[i + 1] for i in range(len(self.preturi_desc) - 1))
        assert self.preturi_desc_check == True

    def check_sort_alfabetic_ascending(self):
        self.nume_produse = []
        for nume in self.driver.find_elements(*ProductsPageLocators.PRODUCTS_NAMES):
            self.nume_produse.append(nume.text)
        sorted_names = sorted(self.nume_produse)
        assert sorted_names == self.nume_produse, 'Sorting after name (asc) is not correct.'

    def check_sort_alfabetic_descending(self):
        self.nume_produse = []
        for nume in self.driver.find_elements(*ProductsPageLocators.PRODUCTS_NAMES):
            self.nume_produse.append(nume.text)
        sorted_names = sorted(self.nume_produse, reverse=True)
        assert sorted_names == self.nume_produse, 'Sorting after name (desc) is not correct.'

    def check_sort_discount_desc(self):
        self.products_with_discount = self.driver.find_elements(*ProductsPageLocators.DISCOUNT_PRODUCTS)
        self.discount_list_products= []
        for item in self.products_with_discount:
            self.discount_list_products.append(item.text)
        self.discount_list_products_int = [int(x.strip('%')) for x in self.discount_list_products]
        assert self.discount_list_products_int == sorted(self.discount_list_products_int, reverse=True)

    def check_sort_discount_asc(self):
        self.products_with_discount = self.driver.find_elements(*ProductsPageLocators.DISCOUNT_PRODUCTS)
        self.discount_list_products= []
        for item in self.products_with_discount:
            self.discount_list_products.append(item.text)
        self.discount_list_products_int = [int(x.strip('%')) for x in self.discount_list_products]
        assert self.discount_list_products_int == sorted(self.discount_list_products_int)

    def sort_in_stoc_items(self):
        time.sleep(1)
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_IN_STOC)
        button.click()
        time.sleep(1)

    def check_items_number_on_page(self):
        lista_produse = []
        for produs in self.driver.find_elements(*ProductsPageLocators.PRODUCTS_NAMES):
            self.nume_produse.append(produs)
        text_for_check = self.driver.find_element(*ProductsPageLocators.TEXT_NUMBER_OF_PRODUCTS_ON_PAGE).text
        assert len(lista_produse) <= int(text_for_check), 'Number of objects on the page is bigger then selected'

    def add_book_1(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BOOK_1)
        button.click()
        add = self.wait_for_clickable_element(ItemPageLocators.BTN_ADD_PRODUCT_IN_CART)
        add.click()

    def add_book_2(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BOOK_2)
        button.click()
        add = self.wait_for_clickable_element(ItemPageLocators.BTN_ADD_PRODUCT_IN_CART)
        add.click()

    def click_on_cart_button(self):
        cart_btn = self.wait_for_clickable_element(HomePageLocators.BTN_CART)
        cart_btn.click()


    def check_items_number_on_cart(self):
        self.click_on_cart_button()
        number_on_cart = self.wait_for_displayed_element(HomePageLocators.CART_PRODUCTS_NUMBER).text
        items_added = []
        number_of_items_added = self.driver.find_elements(*ProductsPageLocators.NUMBER_OF_PRODUCTS_IN_THE_CART)
        for item in number_of_items_added:
            items_added.append(int(item.text))
        sum_items = sum(items_added)
        assert int(number_on_cart) == int(sum_items), 'The number of added objects is not the same with the one from cart icon'



    def click_pe_stoc_limitat_sorting(self):
        time.sleep(1)
        stoc_limitat_button = self.driver.find_element(By.XPATH, '//*[@id="coloana-filtre"]/filter-form/div/form/div[1]/div/md-checkbox[3]')
        stoc_limitat_button.click()


    def check_if_in_stoc_btn_is_active(self):
        IN_STOC_BTN = self.driver.find_element(By.XPATH,'//*[@id="coloana-filtre"]/filter-form/div/form/div[1]/div/md-checkbox[2]')
        BUTON_ACTIVAT_STATUS = IN_STOC_BTN.get_attribute('aria-checked')
        try:
            assert BUTON_ACTIVAT_STATUS == "false", 'Button "In stoc" is activ'
        except AssertionError as error:
            print(error)
        return BUTON_ACTIVAT_STATUS
    def check_if_stoc_limitat_btn_is_active(self):
        STOC_LIMITAT_BTN = self.driver.find_element(By.XPATH,'//*[@id="coloana-filtre"]/filter-form/div/form/div[1]/div/md-checkbox[3]')
        BUTON_ACTIVAT_STATUS = STOC_LIMITAT_BTN.get_attribute('aria-checked')
        try:
            assert BUTON_ACTIVAT_STATUS == "false", 'Button "Stoc-limitat" is activ.'
        except AssertionError as error:
            print(error)
        return BUTON_ACTIVAT_STATUS
    def check_if_livrare_24h_btn_is_active(self):
        LIVRARE_24H_BTN = self.driver.find_element(By.XPATH,
                                                   '//*[@id="coloana-filtre"]/filter-form/div/form/div[1]/div/md-checkbox[1]')
        BUTON_ACTIVAT_STATUS = LIVRARE_24H_BTN.get_attribute('aria-checked')
        try:
            assert BUTON_ACTIVAT_STATUS == "false", 'Button "Livrare 24h" is activ'
        except AssertionError as error:
            print(error)
        return BUTON_ACTIVAT_STATUS

    def check_disponibility_sort_buttons(self):
        butoane_active = []
        butoane_active.append(self.check_if_in_stoc_btn_is_active())
        butoane_active.append(self.check_if_stoc_limitat_btn_is_active())
        butoane_active.append(self.check_if_livrare_24h_btn_is_active())
        butoane_active_count = butoane_active.count('true')
        assert butoane_active_count == 3, f"Expected 1 button active but {butoane_active_count} are active."

    def check_author_relevance_products_received(self, text):
        time.sleep(1)
        objects_with_author = []
        web_authors = self.driver.find_elements(*ProductsPageLocators.PRODUCTS_AUTHORS)
        for autor in web_authors:
            objects_with_author.append(autor.text.lower())

        nr_produse_conform_textului = 0
        for product in objects_with_author:
             if text in product:
                 nr_produse_conform_textului += 1
             else:
                 pass

        percentage = (nr_produse_conform_textului / len(objects_with_author) ) * 100
        assert percentage > 50, "Under 50% of products showed have other auhtor name."

    def check_name_relevance_products_received(self, text):
        time.sleep(1)
        objects_with_name = []
        web_names_products = self.driver.find_elements(*ProductsPageLocators.PRODUCTS_NAMES)
        for name in web_names_products:
            objects_with_name.append(name.text.lower())

        nr_produse_conform_textului = 0
        for product in objects_with_name:
            if text in product:
                nr_produse_conform_textului += 1
            else:
                pass

        percentage = (nr_produse_conform_textului / len(objects_with_name)) * 100
        assert percentage > 50, "Under 50% of products showed have no text similarity in title/name."

    def click_on_first_item(self):
        time.sleep(0.5)
        items_on_page = self.driver.find_elements(*ProductsPageLocators.PRODUCTS_NAMES)
        item_to_add = items_on_page[1]
        item_to_add.click()

    def click_on_second_item(self):
        time.sleep(1)
        items_on_page = self.driver.find_elements(*ProductsPageLocators.PRODUCTS_NAMES)
        item_to_add = items_on_page[1]
        item_to_add.click()
    def click_remove_in_cart(self):
        self.driver.find_element(*HomePageLocators.BTN_REMOVE_FIRST_PRODUCT).click()
        time.sleep(1)

    def check_price_in_cart(self):
        time.sleep(0.5)
        preturi_in_cart = []
        prices_elements = self.driver.find_elements(*ProductsPageLocators.PRICES_IN_CART)
        for price in prices_elements:
            preturi_in_cart.append(price.text)
        suma_preturi = 0
        for pret in preturi_in_cart:
            suma_preturi += float(pret.replace(',', '.'))
        final_price_in_cart = self.driver.find_element(*ProductsPageLocators.FINAL_PRICE).text
        final_price_in_cart_float = float(final_price_in_cart.replace(',', '.'))
        assert float(suma_preturi) == final_price_in_cart_float, "Price wrongly displayed"

    def go_to_checkout_page(self):
        btn_for_checkout = self.wait_for_clickable_element(ProductsPageLocators.BTN_GO_TO_CHECKOUT)
        btn_for_checkout.click()
        time.sleep(1)