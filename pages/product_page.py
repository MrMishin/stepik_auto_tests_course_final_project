import time
from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators

class ProductPage(BasePage):
    def test_user_can_add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()
        self.check_product_name()
        self.check_product_price()

    def test_user_can_add_product_to_basket_promo(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()
        self.solve_quiz_and_get_code() # Calculation for promo
        self.check_product_name()
        self.check_product_price()

    # Проверка наличия кнопки добавления в заказ
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"

    # Добавление товара в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        self.browser.implicitly_wait(2)

    #Проверка имени продукта
    def check_product_name(self):
        #self.browser.implicitly_wait(2)
        product_name = self.browser.find_element(*ProductPageLocators.PROD_NAME).text
        product_name_msg = self.browser.find_element(*ProductPageLocators.PROD_MSG_NAME).text
        assert product_name_msg == product_name,"Wrong product name"

    #Проверка цены продукта
    def check_product_price(self):
        #self.browser.implicitly_wait(2)
        product_price = self.browser.find_element(*ProductPageLocators.PROD_PRICE).text
        product_price_msg = self.browser.find_element(*ProductPageLocators.PROD_MSG_PRICE).text
        assert product_price == product_price_msg, "Wrong product price"

    # Проверка на отсутствие элемента (упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый)
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"

    # Проверка на отсутствие элемента (будет ждать до тех пор, пока элемент не исчезнет)
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should disappear"