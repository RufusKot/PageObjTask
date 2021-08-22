from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')


class ProductPageLocators():
    ADD_TO_BSK_BTN = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRICE_ADDED_TO_BSK = (By.CSS_SELECTOR, '#messages div:nth-child(3) .alertinner strong')
    IS_IN_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    WHAT_TO_ADD_NAME = (By.CSS_SELECTOR, '.product_main h1')
    WHAT_TO_ADD_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
