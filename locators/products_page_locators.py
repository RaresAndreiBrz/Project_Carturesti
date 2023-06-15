from selenium.webdriver.common.by import By


class ProductsPageLocators:
    # general locators
    PRETURI_PRODUSE = (By.CLASS_NAME, "suma")
    NUME_PRODUSE = (By.XPATH, '//*[@class="md-title ng-binding"]')
    AUTORI_PRODUSE = (By.XPATH, '//*[@class ="subtitlu-produs ng-binding"]')

    # sorting locators
    BTN_SORT1 = (By.XPATH,
                 '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/grid-filter-sortby/md-input-container/md-select/md-select-value/span[1]/div/span')
    BTN_SORT_PRET_ASC = (By.XPATH, '//md-option[@value="price asc"]')
    BTN_SORT_PRET_DESC = (By.XPATH, '//md-option[@value="price desc"]')
    BTN_SORT_ALFAB_ASC = (By.XPATH, '//md-option[@value="name_s asc"]')
    BTN_SORT_ALFAB_DESC = (By.XPATH, '//md-option[@value="name_s desc"]')
    BTN_SORT_DISCOUNT_ASC = (
        By.XPATH,
        '//md-option[@value="if(sub(list_price, price), div(sub(list_price, price), list_price), 100.0 ) asc"]')
    BTN_SORT_DISCOUNT_DESC = (
        By.XPATH, '//md-option[@value="if(list_price, div(sub(list_price, price), list_price), 0) desc"]')

    BTN_SORT2 = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/grid-filter-perpage/md-input-container/md-select/md-select-value/span[1]/div/span")
    BTN_30_ITEMS = (By.XPATH, "/html/body/div[7]/md-select-menu/md-content/md-option[1]/div[1]/span")
    BTN_60_ITEMS = (By.XPATH, "/html/body/div[7]/md-select-menu/md-content/md-option[2]/div/span")
    BTN_90_ITEMS = (By.XPATH, "/html/body/div[7]/md-select-menu/md-content/md-option[3]/div/span")
    TEXT_NUMBER_ITEMS_ON_PAGE = (By.XPATH,
                                 '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/grid-filter-perpage/md-input-container/md-select/md-select-value/span[1]/div/span')

    NUMAR_PRODUSE_ADAUGATE_IN_COS = (By.XPATH, "//span[@data-ng-bind='p.quantity']")
    # disponibilitate sort
    BTN_IN_STOC = (By.XPATH, '//*[@id="coloana-filtre"]/filter-form/div/form/div[1]/div/md-checkbox[2]')

    #cartea_1 pentru verificarea numarului de obiecte in cos
    CARTEA_1 = (By.XPATH, '//*[@content="/carte/12-rules-for-life-302799900?p=2"]')
    # cartea_1 pentru verificarea numarului de obiecte in cos
    CARTEA_2 = (By.XPATH, '//*[@content="/carte/dincolo-de-ordine-1037305993?p=3"]')

    PRICES_IN_CART = (By.XPATH, '//*[@data-ng-bind="numberFormat(p.price)"]')
    FINAL_PRICE = (By.XPATH, '// *[ @data-ng-bind = "numberFormat(cart.total)"]')
    TO_CHECKOUT_BTN = (By.XPATH, '//*[@class="md-raised alt butonFinalizare md-button ng-scope md-ink-ripple"]')