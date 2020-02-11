from .base_page import BasePage
from .locators import ProductPageLocator
import time


class ProductPage(BasePage):

    def click_add_to_cart_button(self):
        add_to_cart = self.browser.find_element(*ProductPageLocator.ADD_BUTTON)
        add_to_cart.click()

    # For New Year Promo pages. With quiz modal window
    def check_add_to_cart(self):
        self.click_add_to_cart_button_promo()
        self.should_be_same_order_title_in_cart()
        self.should_be_same_order_price_in_cart()

    # For regural actions. Add to cart some product.
    def check_regular_adding_to_cart(self):
        self.click_add_to_cart_button()
        self.should_not_be_success_message()

    def click_add_to_cart_button_promo(self):
        add_to_cart = self.browser.find_element(*ProductPageLocator.ADD_BUTTON)
        add_to_cart.click()
        self.solve_quiz_and_get_code()
        time.sleep(3)

    def check_product_page_for_success_message(self):
        self.should_not_be_success_message()

    def check_regular_adding_to_cart_with_disappearing(self):
        self.click_add_to_cart_button()
        self.should_not_be_success_message_with_disappearing()

    def should_be_same_order_title_in_cart(self):
        order_title = self.browser.find_element(*ProductPageLocator.ORDER_TITLE)        
        in_alert_order_title = self.browser.find_element(*ProductPageLocator.ALERT_ORDER_TITLE)        
        assert order_title.text == in_alert_order_title.text, "Order titles not identical"

    def should_be_same_order_price_in_cart(self):
        pass

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_with_disappearing(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
