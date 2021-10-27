import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    first_name = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name.send_keys("Petrov")
    city = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    city.send_keys("Smolensk")
    country = browser.find_element(By.XPATH, "//input[@id='country']")
    country.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    time.sleep(6)
    browser.quit()
