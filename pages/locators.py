from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")

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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, 'a[href*="basket"]')
    BASKET_EMPTY = (By.XPATH, '//p[contains(text(),"Your basket is empty.")]')
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")




