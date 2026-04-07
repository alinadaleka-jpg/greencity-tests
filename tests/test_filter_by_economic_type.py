import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGreenCityEventsFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_tc2_filter_by_economic_type(self):
        """
        TC-2: Перевірка вибору категорії фільтрації 'Економічний'
        """
        filter_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'filter-container')]//mat-select"))
        )
        filter_button.click()

        economic_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), 'Економічний')]"))
        )
        economic_option.click()

        applied_filter_tag = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'mat-mdc-chip-chip')]//span[contains(text(), 'Економічний')]"))
        )

        self.assertTrue(applied_filter_tag.is_displayed(),
                        "Фільтр 'Економічний' не був застосований або тег не з'явився.")

        results_text = self.driver.find_element(By.CLASS_NAME, "count").text
        self.assertIn("Знайдено", results_text)

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()