import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        print('shakalakabuka')
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.browser.get(link)
        login_page = LoginPage(self.browser, link)
        login_page.register_new_user()
        login_page.should_be_authorized_user()


    #@pytest.mark.parametrize('last_num', ['1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])  - параметаризация
    def test_user_can_add_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_basket()
        page.check_if_added_to_basket()
        self.browser.implicitly_wait(5)
        page.check_correct_price()

    def test_user_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()



# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.should_not_be_success_message()
#
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.success_message_disappeared()
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     l_page =LoginPage(browser, browser.current_url)
#     l_page.should_be_login_page()