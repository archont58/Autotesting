import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

with open("test.txt", "w") as file:
    content = file.write("automationbypython")

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ivanov")
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys("Ivanov@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "input#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    time.sleep(4)
    browser.quit()
