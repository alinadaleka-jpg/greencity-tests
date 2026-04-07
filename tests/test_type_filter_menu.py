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

    def test_tc1_open_event_type_filter_menu(self):
        """
        TC-1: Перевірка, що кнопка 'Тип події' активує список категорій.
        """
        filter_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "mat-select-6"))
        )

        filter_button.click()

        dropdown_menu = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-select-panel"))
        )

        self.assertTrue(dropdown_menu.is_displayed(), "Меню фільтрації не відкрилося після кліку.")

        options = dropdown_menu.find_elements(By.TAG_NAME, "mat-option")
        self.assertGreater(len(options), 0, "Список категорій порожній.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()