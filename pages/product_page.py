import time
from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def test_user_can_add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()
        self.check_product_name()
        self.check_product_price()


    # Проверка наличия кнопки добавления в заказ
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"

    # Добавление товара в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
        self.browser.implicitly_wait(2)


    #Проверка имени продукта
    def check_product_name(self):
        self.browser.implicitly_wait(2)
        product_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        product_name_msg = self.browser.find_element(*ProductPageLocators.PROD_MSG_NAME).text
        assert product_name_msg == product_name,"Wrong product name"

    #Проверка цены продукта
    def check_product_price(self):
        self.browser.implicitly_wait(2)
        product_price = self.browser.find_element(*ProductPageLocators.PROD_PRICE).text
        product_price_msg = self.browser.find_element(*ProductPageLocators.PROD_MSG_PRICE).text
        assert product_price == product_price_msg, "Wrong product price"