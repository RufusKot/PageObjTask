from .base_page import BasePage
import time
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.add_to_basket_btn)
        add.click()
        self.solve_quiz_and_get_code()

    def what_to_add(self):
        text = self.browser.find_element(*ProductPageLocators.what_to_add_name).text
        price = self.browser.find_element(*ProductPageLocators.what_to_add_price).text
        return text, price

    def check_if_added_to_basket(self):
        text = self.browser.find_element(*ProductPageLocators.is_in_basket).text
        assert text == self.what_to_add()[0], 'Expected book not in basket'

    def check_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.what_to_add_price).text
        assert price == self.what_to_add()[1], 'Expected basket total is invalid'
