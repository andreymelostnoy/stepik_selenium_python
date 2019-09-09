from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True

    # link = "http://suninjuly.github.io/selects1.html"
    # browser = webdriver.Chrome()
    # browser.get(link)
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # x = browser.find_element_by_css_selector("#num1").text
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
