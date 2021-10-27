import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    browser.switch_to.alert.accept()
    answer = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    print(browser.switch_to.alert.text)
    browser.quit()
