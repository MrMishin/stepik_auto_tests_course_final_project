from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def test_guest_not_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def test_guest_empty_basket_msg(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Empty basket massage is not exist"