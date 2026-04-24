# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage:
#     BASE_URL = "https://www.greencity.cx.ua/#/greenCity"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 20)
#
#     def open(self, path=""):
#         self.driver.get(self.BASE_URL + path)
#
#     def find(self, by, value):
#         return self.wait.until(EC.presence_of_element_located((by, value)))
#
#     def find_clickable(self, by, value):
#         return self.wait.until(EC.element_to_be_clickable((by, value)))
#
#     def find_all(self, by, value):
#         self.wait.until(EC.presence_of_element_located((by, value)))
#         return self.driver.find_elements(by, value)
#
#     def js_click(self, element):
#         self.driver.execute_script("arguments[0].click();", element)
#
#     def js_scroll_into_view(self, element):
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#
#     def wait_invisible(self, by, value):
#         return self.wait.until(EC.invisibility_of_element_located((by, value)))
#
#     def wait_visible(self, by, value):
#         return self.wait.until(EC.visibility_of_element_located((by, value)))

import unittest
from tests.base_test import BaseTest
from pages.events_page import EventsPage


class TestTC3SelectAll(BaseTest):
    """TC-3: кнопка 'Всі типи' виділяє всі категорії і оновлює результати."""

    ALL_LABELS = ["Економічний", "Соціальний", "Екологічний"]
    ALL_OPTIONS = [
        EventsPage.OPTION_ECONOMIC,
        EventsPage.OPTION_SOCIAL,
        EventsPage.OPTION_ECOLOGY,
    ]

    def test_select_all_event_types(self):
        self.page.open_type_filter()
        self.page.select_option(EventsPage.OPTION_ALL)

        for locator, label in zip(self.ALL_OPTIONS, self.ALL_LABELS):
            self.assertTrue(
                self.page.is_option_selected(locator),
                f"Опція '{label}' не вибрана після кліку 'Всі типи'.",
            )

        for label in self.ALL_LABELS:
            self.assertTrue(
                self.page.is_filter_chip_visible(label),
                f"Чіп '{label}' не з'явився після вибору 'Всі типи'.",
            )

        self.assertIn(
            "Знайдено",
            self.page.get_results_counter_text(),
            "Лічильник 'Знайдено' не відображається після вибору всіх типів.",
        )


if __name__ == "__main__":
    unittest.main()