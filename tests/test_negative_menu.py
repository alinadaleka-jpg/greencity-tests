# from test_pmo.base_test import BaseTest
#
#
# class TestMenuNegative(BaseTest):
#
#     def test_tc1_menu_closes_on_second_click(self):
#
#         self.page.click_filter_button()
#         self.page.wait_until_options_visible()
#
#         self.page.click_filter_button_second_time()
#
#         is_closed = self.page.is_filter_closed()
#         self.assertTrue(is_closed)

import unittest
from tests.base_test import BaseTest


class TestTC1NegativeMenu(BaseTest):
    """TC-1 Negative: меню фільтрації закривається після повторного кліку."""

    def test_menu_closes_on_second_click(self):
        self.page.open_type_filter()
        self.page.close_type_filter()
        self.assertTrue(
            self.page.is_overlay_closed(),
            "Меню фільтрації залишилося відкритим після повторного кліку.",
        )


if __name__ == "__main__":
    unittest.main()