from .base_page import BasePage
from .locators import MainPageLocator
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocator.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_presented(*MainPageLocator.LOGIN_LINK), "Login link is not presented"
