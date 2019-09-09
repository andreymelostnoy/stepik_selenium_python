from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12 * math.sin(int(
        browser.find_element_by_css_selector("#treasure").get_attribute("valuex")))))))
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
