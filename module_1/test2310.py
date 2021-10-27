import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, "div.form-group.first_class > input[required]")
    lastname = browser.find_element(By.CSS_SELECTOR, "div.form-group.second_class > input[required]")
    email = browser.find_element(By.CSS_SELECTOR, "div.form-group.third_class > input[required]")
    button = browser.find_element(By.CSS_SELECTOR, "form > button")

    firstname.send_keys("Ivan")
    lastname.send_keys("Ivanov")
    email.send_keys("ivan@gmail.com")
    button.click()

    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1")

    assert "Congratulations! You have successfully registered!" == welcome_text.text

    time.sleep(3)
    browser.quit()

