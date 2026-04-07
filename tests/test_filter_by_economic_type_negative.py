import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestGreenCityEventsFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_tc2_negative_filter_not_present_by_default(self):
        """
        Перевірка, що'Економічний' відсутній,
        якщо ми не взаємодіяли з фільтром.
        """
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'mat-mdc-chip-chip')]//span[contains(text(), 'Економічний')]"))
            )
            self.fail("Фільтр 'Економічний' відображається, хоча він не був обраний.")
        except TimeoutException:
            pass

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()