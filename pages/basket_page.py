from .base_page import BasePage
from .locators import BasketPageLocator
import pytest


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_element_presented(*BasketPageLocator.EMPTY_BASKET), \
            "Basket is not empty"

    def should_not_be_empty_basket(self):
        assert not self.is_not_element_present(*BasketPageLocator.NOT_EMPTY_BASKET), \
            "Basket is empty"
