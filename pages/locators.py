from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#id_login-username')
    register_form = (By.CSS_SELECTOR, '#id_registration-email')

class ProductPageLocators():
    add_to_basket_btn = (By.CSS_SELECTOR, '#add_to_basket_form button')
    price_added_to_basket = (By.CSS_SELECTOR, '#messages .alertinner strong')
    is_in_basket = (By.CSS_SELECTOR, '#messages .alert-success strong')
    what_to_add_name = (By.CSS_SELECTOR, '.product_main h1')
    what_to_add_price = (By.CSS_SELECTOR, '.product_main .price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")