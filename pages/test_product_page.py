from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element_by_css_selector()
        add.click()
        self.solve_quiz_and_get_code()

    def check_if_in_basket(self):

    def check_correct_price(self):