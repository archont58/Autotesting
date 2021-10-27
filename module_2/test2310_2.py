import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    valuex = treasure.get_attribute("valuex")
    form_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")

    answer = calc(valuex)
    form_answer.send_keys(answer)
    robot_checkbox.click()
    robot_radiobutton.click()
    submit_button.click()

    time.sleep(4)
    browser.quit()

