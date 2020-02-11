from .base_page import BasePage
from .locators import LoginPageLocator
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == LoginPageLocator.LOGIN_URL, \
            "Login url is invalid"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocator.LOGIN_FORM), \
            "Login form is not presented on page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocator.REGISTER_FORM), \
            "Register form is not presented on page"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.XPATH, "//div[contains(@class, 'register_form')]//input[@type='email']")
        password_input1 = self.browser.find_element_by_xpath("//div[contains(@class, 'register_form')]//input[@name='registration-password1']")
        password_input2 = self.browser.find_element_by_xpath("//div[contains(@class, 'register_form')]//input[@name='registration-password2']")
        signup = self.browser.find_element_by_xpath("//button[@name='registration_submit']")
        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        signup.click()
