import pytest
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.product_name_in_message_and_in_basket()
    product_page.basket_cost_equals_product_cost()


#@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     product_page = ProductPage(browser, link)
     product_page.open()
     product_page.add_product_to_basket()
     product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_message_should_disappear()
