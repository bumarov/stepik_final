from selenium.webdriver.common.by import By


class BasePageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini pull-right')]//a[@class='btn btn-default']")


class LoginPageLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class ProductPageLocator():
    PROMO_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    REGULAR_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ORDER_TITLE = (By.CSS_SELECTOR, "h1")
    ALERT_ORDER_TITLE = (By.CSS_SELECTOR, "div.alertinner strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alertinner')]")


class BasketPageLocator():
    EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']//p/a")
