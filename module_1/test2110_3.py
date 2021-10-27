import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block > input")
    #print(elements)
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "form > button")
    button.click()
    time.sleep(5)
    browser.quit()

