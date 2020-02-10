from .base_page import BasePage
from .locators import BasketPageLocator


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_element_presented(*BasketPageLocator.EMPTY_BASKET), \
            "Basket is not empty"
