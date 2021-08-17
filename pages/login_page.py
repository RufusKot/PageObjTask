from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'url is invalid, does not contain "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), 'no login form on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), 'no registration form on the page'