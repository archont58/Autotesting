from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Message is present!"

    def should_be_empty_basket_message(self):
        try:
            assert "Your basket is empty" in self.browser.find_element \
                (*BasketPageLocators.MESSAGE_EMPTY_BASKET).text, "Basket isn't empty!"
        except NoSuchElementException:
            False