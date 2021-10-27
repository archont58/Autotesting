import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # открытие браузера и переход по ссылке
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск веб-элементов
    firstname = browser.find_element(By.CSS_SELECTOR, "div.form-group.first_class > input[required]")
    lastname = browser.find_element(By.CSS_SELECTOR, "div.form-group.second_class > input[required]")
    email = browser.find_element(By.CSS_SELECTOR, "div.form-group.third_class > input[required]")
    button = browser.find_element(By.CSS_SELECTOR, "form > button")

    # заполнение форм и отправка
    firstname.send_keys("Ivan")
    lastname.send_keys("Ivanov")
    email.send_keys("ivan@gmail.com")
    button.click()
    time.sleep(1)

    # проверяем совпадение ожидаемого и фактического текстов
    welcome_text = browser.find_element(By.TAG_NAME, "h1")
    assert "Congratulations! You have successfully registered!" == welcome_text.text

finally:
    time.sleep(3)
    browser.quit()
