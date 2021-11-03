import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("Start browser")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("Quit browser")
    browser.quit()