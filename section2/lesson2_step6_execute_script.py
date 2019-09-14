from selenium import webdriver
import time
import math


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    result = math.log(abs(12 * math.sin(int(x))))
    browser.find_element_by_css_selector("#answer").send_keys(str(result))
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    button.click()
    assert True

finally:
    time.sleep(5)
    browser.quit()
