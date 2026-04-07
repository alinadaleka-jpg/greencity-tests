import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGreenCityEventsBulkSelect(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_tc3_select_all_event_types(self):
        """
        TC-3: Перевірка функціонала кнопки 'Всі типи'
        """
        filter_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'filter-container')]//mat-select"))
        )
        filter_button.click()

        select_all_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//mat-option//span[contains(text(), 'Всі типи')]"))
        )
        select_all_option.click()

        options = self.driver.find_elements(By.TAG_NAME, "mat-option")

        for option in options:
            is_selected = option.get_attribute("aria-selected")
            self.assertEqual(is_selected, "true", f"Опція {option.text} не була вибрана після натискання 'Всі типи'")

        applied_chips = self.driver.find_elements(By.CLASS_NAME, "mat-mdc-chip-chip")
        self.assertGreater(len(applied_chips), 1, "Має бути більше одного активного фільтра")

    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()