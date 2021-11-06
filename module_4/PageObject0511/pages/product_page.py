from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def product_name_in_message_and_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text, "Product name in message is incorrect!"

    def basket_cost_equals_product_cost(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Basket price and product price aren't equals!"






