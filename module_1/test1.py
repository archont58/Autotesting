import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

textarea = driver.find_element(By.XPATH, "//textarea")
textarea.send_keys("get()")
time.sleep(5)
submit_button = driver.find_element(By.XPATH, '//*[@id="ember222"]/div/section/div/div[1]/div[4]/button')

submit_button.click()
time.sleep(5)
driver.quit()
