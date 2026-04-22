# tests/test_tc1_tc2_negative.py

from pages.events_page import EventsPage


def test_tc1_negative_menu_closes_on_second_click(driver):
    """TC-1: Меню закривається після повторного кліку"""
    page = EventsPage(driver).open()

    page.close_filter_with_second_click()

    assert page.is_dropdown_closed(), \
        "Меню залишилося відкритим після повторного кліку."


def test_tc2_negative_economic_filter(driver):
    """TC-2: Перевірка вибору категорії фільтрації 'Економічний'"""
    page = EventsPage(driver).open()

    page.open_type_filter()
    page.select_economic_filter()

    chip = page.get_chip("Економічний")
    assert chip.is_displayed(), "Фільтр 'Економічний' не був застосований."

    assert "Знайдено" in page.get_results_counter_text()