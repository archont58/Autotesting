import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    first_name = browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) > input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "div:nth-child(2) > input")
    last_name.send_keys("Petrov")
    city = browser.find_element(By.CSS_SELECTOR, "div:nth-child(3) > input")
    city.send_keys("Smolensk")
    country = browser.find_element(By.CSS_SELECTOR, "div:nth-child(4) > input")
    country.send_keys("Russia")
    submit_button = browser.find_element(By.ID, "submit_button")
    submit_button.click()
    time.sleep(5)
    browser.quit()
