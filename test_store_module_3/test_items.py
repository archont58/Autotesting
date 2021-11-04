from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_store(browser):
    browser.get(link)
    time.sleep(5)     # убедиться во время задержки, что язык страницы соответствует переданной локали
    try:
        submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    except NoSuchElementException:
        submit_button = None
    assert submit_button is not None, "The button was not found!"
