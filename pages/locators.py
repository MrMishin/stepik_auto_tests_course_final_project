from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    PROD_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PROD_MSG_NAME = (By.CSS_SELECTOR, 'div#messages div:nth-child(1) div.alertinner strong')
    PROD_PRICE = (By.CSS_SELECTOR, 'div.product_main .price_color')
    PROD_MSG_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


