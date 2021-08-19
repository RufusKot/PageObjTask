from .base_page import BasePage
import time
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.add_to_basket_btn)
        add.click()
        self.solve_quiz_and_get_code()
        time.sleep(40)

    # def check_if_in_basket(self):
    #
    # def check_correct_price(self):