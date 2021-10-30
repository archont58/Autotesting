import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    correct_congratulation = "Congratulations! You have successfully registered!"

    def test_first_link(self):
        browser = webdriver.Chrome()
        browser.get(TestRegistration.link1)
        browser.find_element(By.CSS_SELECTOR, "div.form-group.first_class > input[required]").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "div.form-group.second_class > input[required]").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, "div.form-group.third_class > input[required]").send_keys("ivan@gmail.com")
        browser.find_element(By.CSS_SELECTOR, "form > button").click()
        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text, TestRegistration.correct_congratulation, "Registration failed!")
        browser.quit()

    def test_second_link(self):
        browser = webdriver.Chrome()
        browser.get(TestRegistration.link2)
        browser.find_element(By.CSS_SELECTOR, "div.form-group.first_class > input[required]").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "div.form-group.second_class > input[required]").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, "div.form-group.third_class > input[required]").send_keys("ivan@gmail.com")
        browser.find_element(By.CSS_SELECTOR, "form > button").click()
        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text, TestRegistration.correct_congratulation, "Registration failed!")
        browser.quit()

if __name__ == "__main__":
    unittest.main()