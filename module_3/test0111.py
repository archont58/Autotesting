import math, time, pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc():
    answer = math.log(int(time.time()))
    return str(answer)

correct_answer = "Correct!"

@pytest.fixture(scope="function")
def browser():
    print("Start browser")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("Quit browser")
    browser.quit()


class TestStepik:
    @pytest.mark.parametrize('number', ["236895", "236896", "236898", "236897", "236899", "236903", "236904", "236905"])
    def test_feedback(self, browser, number):
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(calc())
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        fact_answer = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        assert fact_answer == correct_answer, f"Answer incorrect! Fact answer: {fact_answer}, expected: {correct_answer}"
