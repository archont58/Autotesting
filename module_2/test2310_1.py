import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/math.html")
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    form_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "div.form-check.form-check-custom > label")
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, "div.form-check.form-radio-custom > label")
    submit_button = browser.find_element(By.CSS_SELECTOR, "form > button.btn.btn-default")

    answer = calc(x.text)
    form_answer.send_keys(answer)
    robot_checkbox.click()
    robot_radiobutton.click()
    submit_button.click()

    time.sleep(4)
    browser.quit()



