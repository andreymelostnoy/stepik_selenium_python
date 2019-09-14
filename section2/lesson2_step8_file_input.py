from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name='firstname']").send_keys("Ivan")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("Petrov")
    browser.find_element_by_css_selector("[name='email']").send_keys("a@b.c")
    browser.find_element_by_css_selector("#file").send_keys(os.path.abspath("file_to_upload.txt"))

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
