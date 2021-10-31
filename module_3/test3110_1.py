import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
    print("Start browser")
    browser = webdriver.Chrome()
    yield browser
    print("Quit browser")
    browser.quit()

class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        print("Start Test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("Finish test1")


    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("Start Test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("Finish test2")
