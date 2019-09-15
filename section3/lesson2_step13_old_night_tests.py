from selenium import webdriver
import unittest


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        try:
            self.browser = webdriver.Chrome()
            self.browser.get("http://suninjuly.github.io/registration1.html")

            self.browser.find_element_by_css_selector(".first_block input.first").send_keys("Ivan")
            self.browser.find_element_by_css_selector(".first_block input.second").send_keys("Petrov")
            self.browser.find_element_by_css_selector(".first_block input.third").send_keys("ivan@petrov.ru")

            button = self.browser.find_element_by_css_selector("button.btn")
            button.click()

            welcome_text = self.browser.find_element_by_tag_name("h1").text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            self.browser.quit()

    def test_registration2(self):
        try:
            self.browser = webdriver.Chrome()
            self.browser.get("http://suninjuly.github.io/registration2.html")

            self.browser.find_element_by_css_selector(".first_block input.first").send_keys("Ivan")
            self.browser.find_element_by_css_selector(".first_block input.second").send_keys("Petrov")
            self.browser.find_element_by_css_selector(".first_block input.third").send_keys("ivan@petrov.ru")

            button = self.browser.find_element_by_css_selector("button.btn")
            button.click()

            welcome_text = self.browser.find_element_by_tag_name("h1").text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            self.browser.quit()


if __name__ == "__main__":
    unittest.main()


