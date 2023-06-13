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
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_PRET_ASC)
        button.click()

    def sort_price_desc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_PRET_DESC)
        button.click()

    def sort_alfabet_asc(self):
        self.driver.find_element(*ProductsPageLocators.BTN_SORT_ALFAB_ASC).click()

    def sort_alfabet_desc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_ALFAB_DESC)
        button.click()

    def sort_discount_asc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_DISCOUNT_ASC)
        button.click()

    def sort_discount_desc(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT_DISCOUNT_DESC)
        button.click()

    def click_on_sort_itemsNr_button(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_SORT2)
        button.click()

    def select_30_items_onPage(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_30_ITEMS)
        button.click()

    def select_60_items_onPage(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_60_ITEMS)
        button.click()

    def select_90_items_onPage(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_90_ITEMS)
        button.click()

    def random_sort_of_items_number_on_page(self):
        select_items_random = [self.select_30_items_onPage, self.select_60_items_onPage, self.select_90_items_onPage]
        item_chosen_randomly = random.choice(select_items_random)
        item_chosen_randomly()

    def check_sort_prices_ascending(self):
        time.sleep(1)
        self.preturi_asc = []
        for pret in self.driver.find_elements(*ProductsPageLocators.PRETURI_PRODUSE):
            self.preturi_asc.append(int(float(pret.text)))
        self.preturi_asc_check = all(
            self.preturi_asc[i] <= self.preturi_asc[i + 1] for i in range(len(self.preturi_asc) - 1))
        assert self.preturi_asc_check == True, 'Prices ascending order wrong sorted.'

    def check_sort_prices_descending(self):
        time.sleep(1)
        self.preturi_desc = []
        for pret in self.driver.find_elements(*ProductsPageLocators.PRETURI_PRODUSE):
            self.preturi_desc.append(int(float(pret.text)))
        self.preturi_desc_check = all(
            self.preturi_desc[i] >= self.preturi_desc[i + 1] for i in range(len(self.preturi_desc) - 1))
        assert self.preturi_desc_check == True

    def check_sort_alfabetic_ascending(self):
        self.nume_produse = []
        for nume in self.driver.find_elements(*ProductsPageLocators.NUME_PRODUSE):
            self.nume_produse.append(nume.text)
        sorted_names = sorted(self.nume_produse)
        assert sorted_names == self.nume_produse, 'Sorting after name (asc) is not correct.'

    def check_sort_alfabetic_descending(self):
        self.nume_produse = []
        for nume in self.driver.find_elements(*ProductsPageLocators.NUME_PRODUSE):
            self.nume_produse.append(nume.text)
        sorted_names = sorted(self.nume_produse, reverse=True)
        assert sorted_names == self.nume_produse, 'Sorting after name (desc) is not correct.'

    def sort_in_stoc_items(self):
        time.sleep(1)
        button = self.wait_for_clickable_element(ProductsPageLocators.BTN_IN_STOC)
        button.click()
        time.sleep(1)

    def check_items_number_on_page(self):
        lista_produse = []
        for produs in self.driver.find_elements(*ProductsPageLocators.NUME_PRODUSE):
            self.nume_produse.append(produs)
        text_for_check = self.driver.find_element(*ProductsPageLocators.TEXT_NUMBER_ITEMS_ON_PAGE).text
        assert len(lista_produse) <= int(text_for_check), 'Number of objects on the page is bigger then selected'

    def add_book_JP(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.CARTEA_1)
        button.click()
        add = self.wait_for_clickable_element(ItemPageLocators.BTN_ADD_PRODUS)
        add.click()

    def add_book_JP_2(self):
        button = self.wait_for_clickable_element(ProductsPageLocators.CARTEA_2)
        button.click()
        add = self.wait_for_clickable_element(ItemPageLocators.BTN_ADD_PRODUS)
        add.click()

    def click_on_cart_button(self):
        cart_btn = self.wait_for_clickable_element(HomePageLocators.BTN_CART)
        cart_btn.click()

    def check_items_number_on_cart(self):
        self.click_on_cart_button()
        number_on_cart = self.wait_for_displayed_element(HomePageLocators.CART_ITEMS_NUMBER).text
        items_added = []
        number_of_items_added = self.driver.find_elements(*ProductsPageLocators.NUMAR_PRODUSE_ADAUGATE_IN_COS)
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
        web_authors = self.driver.find_elements(*ProductsPageLocators.AUTORI_PRODUSE)
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
        web_names_products = self.driver.find_elements(*ProductsPageLocators.NUME_PRODUSE)
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