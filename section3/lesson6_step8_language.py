from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def browser():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/")
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
