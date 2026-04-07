import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGreenCitySearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_tc4_search_no_results_parametrized(self):
        invalid_queries = ["qwefyuwh1", "!@#$%", "12345678"]

        for query in invalid_queries:
            with self.subTest(query=query):
                search_field = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input.search-field, input[placeholder*='пошук']"))
                )

                search_field.clear()
                search_field.send_keys(query)
                search_field.send_keys(Keys.ENTER)

                no_results_message = self.wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//*[contains(text(), 'не знайшли жодних результатів')]"))
                )

                self.assertTrue(no_results_message.is_displayed())

                counter = self.driver.find_element(By.CLASS_NAME, "count")
                self.assertIn("0", counter.text)

                search_field.clear()

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()