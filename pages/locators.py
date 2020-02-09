from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class ProductPageLocator():
    PROMO_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ORDER_TITLE = (By.CSS_SELECTOR, "h1")
    ALERT_ORDER_TITLE = (By.CSS_SELECTOR, "div.alertinner strong")
