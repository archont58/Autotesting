import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/execute_script.html")
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    input_form = browser.find_element(By.CSS_SELECTOR, "#answer")
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    answer = calc(int(input_value))

    radiobutton.location_once_scrolled_into_view
    radiobutton.click()
    input_form.send_keys(answer)
    checkbox.click()
    submit_button.location_once_scrolled_into_view
    submit_button.click()
    time.sleep(13)
    browser.quit()
