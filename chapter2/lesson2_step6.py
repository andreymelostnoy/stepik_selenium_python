from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

    # link = "http://suninjuly.github.io/selects1.html"
    # browser = webdriver.Chrome()
    # browser.get(link)
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # x = browser.find_element_by_css_selector("#input_value").text
    # y = browser.find_element_by_css_selector("#num2").text
    # result = int(x) + int(y)
    #
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(str(result))
    #
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
