from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.test_product_page import ProductPage
import time

# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_if_added_to_basket()
    page.check_correct_price()