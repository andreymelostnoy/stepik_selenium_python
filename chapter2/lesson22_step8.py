from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name='firstname']").send_keys("lol")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("kek")
    browser.find_element_by_css_selector("[name='email']").send_keys("che@bu.rek")
    browser.find_element_by_css_selector("#file").send_keys(os.path.abspath("kek.txt"))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
