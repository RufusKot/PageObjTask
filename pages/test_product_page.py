from .base_page import BasePage
import time
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.add_to_basket_btn)
        add.click()
        self.solve_quiz_and_get_code()



    def check_if_added_to_basket(self):
        text = self.browser.find_element(*ProductPageLocators.is_in_basket).text
        assert text == r"The shellcoder's handbook", 'Expected book not in basket'

        # def check_correct_price(self):