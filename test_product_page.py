from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocator


def test_quest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocator.PROMO_URL)
    page.open()
    page.check_add_to_cart()
