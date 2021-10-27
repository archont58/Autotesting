import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x, y):
    return str(x + y)


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum_of_numbers = str(calc(int(num1), int(num2)))
    browser.find_element(By.CSS_SELECTOR, "[value='" + sum_of_numbers + "']").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
    time.sleep(4)
    browser.quit()
