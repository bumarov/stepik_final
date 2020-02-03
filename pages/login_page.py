from .base_page import BasePage
from .locators import LoginPageLocator


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == LoginPageLocator.LOGIN_URL, "Login url is invalid"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocator.LOGIN_FORM), "Login form is not presented on page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocator.REGISTER_FORM), "Register form is not presented on page"
