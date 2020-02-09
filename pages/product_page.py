from .base_page import BasePage
from .locators import ProductPageLocator
# from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):

    def check_add_to_cart(self):
        self.click_add_to_cart_button_promo()
        self.should_be_same_order_title_in_cart()
        self.should_be_same_order_price_in_cart()

    def click_add_to_cart_button_promo(self):
        add_to_cart = self.browser.find_element(*ProductPageLocator.ADD_BUTTON)
        add_to_cart.click()
        self.solve_quiz_and_get_code()
        time.sleep(3)

    def click_add_to_cart_button(self):
        add_to_cart = self.browser.find_element(*ProductPageLocator.ADD_BUTTON)
        add_to_cart.click()

    def should_be_same_order_title_in_cart(self):
        order_title = self.browser.find_element(*ProductPageLocator.ORDER_TITLE)        
        in_alert_order_title = self.browser.find_element(*ProductPageLocator.ALERT_ORDER_TITLE)        
        assert order_title.text == in_alert_order_title.text, "Order titles not identical"

    def should_be_same_order_price_in_cart(self):
        pass

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
