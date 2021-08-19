from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, '#id_login-username')
    register_form = (By.CSS_SELECTOR, '#id_registration-email')

class ProductPageLocators():
    add_to_basket_btn = (By.CSS_SELECTOR, '#add_to_basket_form button')