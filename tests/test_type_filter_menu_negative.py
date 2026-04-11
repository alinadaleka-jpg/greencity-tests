import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGreenCityEvents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_tc1_negative_menu_closes_on_second_click(self):
        """
        Перевірка, що меню фільтрації закривається
        після повторного натискання на кнопку.
        """
        filter_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "mat-select-6"))
        )

        filter_button.click()

        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-select-panel")))

        filter_button.click()

        is_closed = self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-select-panel"))
        )

        self.assertTrue(is_closed, "Меню фільтрації залишилося відкритим після повторного кліку.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
