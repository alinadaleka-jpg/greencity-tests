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

    def test_tc3_negative_none_selected_by_default(self):
        """
        Перевірка, що за замовчуванням жодна опція не вибрана.
        """
        filter_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'filter-container')]//mat-select"))
        )
        filter_button.click()

        options = self.driver.find_elements(By.TAG_NAME, "mat-option")

        for option in options:
            if "Всі типи" in option.text:
                continue

            is_selected = option.get_attribute("aria-selected")
            self.assertEqual(is_selected, "false",
                             f"Опція {option.text} вибрана за замовчуванням, хоча не мала бути.")

        applied_chips = self.driver.find_elements(By.CLASS_NAME, "mat-mdc-chip-chip")
        self.assertEqual(len(applied_chips), 0, "Знайдено активні фільтри, хоча нічого не було обрано.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()