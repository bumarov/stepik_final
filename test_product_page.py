from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocator
from .pages.locators import LoginPageLocator
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_quest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.check_add_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocator.REGULAR_URL)
    page.open()
    page.check_regular_adding_to_cart()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocator.REGULAR_URL)
    page.open()
    page.check_product_page_for_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocator.REGULAR_URL)
    page.open()
    page.check_regular_adding_to_cart_with_disappearing()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/\
            catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        email = str(time.time()) + "@fakemail.org"
        password = "Pass" + str(time.time())
        login_page = LoginPage(browser, LoginPageLocator.LOGIN_URL)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(self.browser, ProductPageLocator.REGULAR_URL)
        page.open()
        page.check_product_page_for_success_message()

    @pytest.mark.skip
    def test_user_can_add_product_to_basket(browser):
        page = ProductPage(browser, ProductPageLocator.REGULAR_URL)
        page.open()
        page.check_add_to_cart()
