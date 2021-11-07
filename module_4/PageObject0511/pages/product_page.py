from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def product_name_in_message_and_in_basket(self):
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert name_in_message == name_in_basket, f"Product name in message ({name_in_message}) and name in basket ({name_in_basket}) aren't equals!"

    def basket_cost_equals_product_cost(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, f"Basket price ({basket_price}) and product price ({product_price}) aren't equals!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Message is present!"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message is not disappear!"





