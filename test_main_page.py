import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    #page.should_be_login_link() #Тест на проверку ссылки на логин (до степа 4.2.8)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.go_to_basket_page()
    #В корзине отсутствуют товары
    basket_page.test_guest_not_empty_basket()
    # В корзине есть надпись что корзина пустая
    basket_page.test_guest_empty_basket_msg()


