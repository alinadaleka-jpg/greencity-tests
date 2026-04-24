# import unittest
#
# from pages.events_page import EventsPage
# from tests.driver_factory import make_driver
#
#
# class TestFilterByEconomicType(unittest.TestCase):
#     """
#     TC-2 Positive:
#     Selecting 'Економічний' from the event-type filter must:
#       1. Show an applied filter chip labelled 'Економічний'
#       2. Show the results counter containing 'Знайдено'
#     """
#
#     def setUp(self):
#         self.driver = make_driver()
#         self.events = EventsPage(self.driver)
#         self.events.open_events()
#
#     def test_filter_by_economic_type(self):
#         """TC-2: Перевірка фільтрації подій за типом 'Економічний'"""
#
#         # Step 1 – open the type-filter dropdown
#         self.events.open_type_filter()
#
#         # Step 2 – select 'Економічний'
#         self.events.select_option(EventsPage.OPTION_ECONOMIC)
#
#         # Step 3 – verify filter chip appears
#         chip = self.events.get_filter_chip("Економічний")
#         self.assertTrue(
#             chip.is_displayed(),
#             "Filter chip 'Економічний' did not appear after selection.",
#         )
#
#         # Step 4 – verify results counter is shown
#         counter = self.events.get_results_counter()
#         self.assertIn(
#             "Знайдено",
#             counter.text,
#             f"Expected 'Знайдено' in results counter, got: '{counter.text}'",
#         )
#
#     def tearDown(self):
#         if self.driver:
#             self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()


import unittest
from tests.base_test import BaseTest
from pages.events_page import EventsPage


class TestTC2FilterByEconomicType(BaseTest):

    def test_positive_chip_appears_after_selecting_economic(self):
        """TC-2 Positive: чіп 'Економічний' з'являється після вибору фільтру."""
        self.page.open_type_filter()
        self.page.select_option(EventsPage.OPTION_ECONOMIC)

        self.assertTrue(
            self.page.is_filter_chip_visible("Економічний"),
            "Чіп фільтру 'Економічний' не з'явився після вибору.",
        )

    def test_positive_results_counter_shown_after_economic_filter(self):
        """TC-2 Positive: лічильник результатів відображається після фільтрації."""
        self.page.open_type_filter()
        self.page.select_option(EventsPage.OPTION_ECONOMIC)

        self.assertIn(
            "Знайдено",
            self.page.get_results_counter_text(),
            "Лічильник 'Знайдено' не відображається після застосування фільтру.",
        )

    def test_negative_economic_not_selected_by_default(self):
        """TC-2 Negative: 'Економічний' не обраний за замовчуванням."""
        self.page.open_type_filter()

        self.assertFalse(
            self.page.is_option_selected(EventsPage.OPTION_ECONOMIC),
            "Опція 'Економічний' помічена як вибрана за замовчуванням.",
        )
        self.page.escape_dropdown()


if __name__ == "__main__":
    unittest.main()