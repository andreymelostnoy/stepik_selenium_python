from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.trollface").click()
    browser.switch_to.window(browser.window_handles[1])

    browser.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12 * math.sin(int(
        browser.find_element_by_css_selector("#input_value").text))))))
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
