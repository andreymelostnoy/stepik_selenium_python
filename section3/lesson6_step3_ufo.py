from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


links = {
    "link1": "https://stepik.org/lesson/236895/step/1",
    "link2": "https://stepik.org/lesson/236896/step/1",
    "link3": "https://stepik.org/lesson/236897/step/1",
    "link4": "https://stepik.org/lesson/236898/step/1",
    "link5": "https://stepik.org/lesson/236899/step/1",
    "link6": "https://stepik.org/lesson/236903/step/1",
    "link7": "https://stepik.org/lesson/236904/step/1",
    "link8": "https://stepik.org/lesson/236905/step/1"
}


@pytest.fixture
def browser():
    print("Test starts")
    browser = webdriver.Chrome()
    yield browser
    print("Test ends")
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_ufo(browser, link):
    browser.get(link)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea"))).\
        send_keys(str(math.log(int(time.time()))))

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".submit-submission"))).click()

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".attempt-message_correct")))

    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".smart-hints__hint"))).text == "Correct!", "--- === !!! ERROR !!! === ---"
