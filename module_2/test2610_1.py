import math
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    answer = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)
    browser.quit()
