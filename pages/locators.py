from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class ProductPageLocator():
    PROMO_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ORDER_TITLE = (By.XPATH, "//h1")
    ALERT_ORDER_TITLE = (By.XPATH, "//div[@class='alertinner']//strong")