
import pytest
from pages.events_page import EventsPage


def test_tc3_select_all_event_types(driver):
    """TC-3: Перевірка функціонала кнопки 'Всі типи'"""
    page = EventsPage(driver).open()

    page.open_type_filter()
    page.select_all_types()

    options = page.get_category_options()
    assert len(options) > 0, "Опції категорій не знайдено"

    for option in options:
        is_selected = option.get_attribute("aria-selected")
        label = option.find_element(*("css selector", "span.mdc-list-item__primary-text")).text
        assert is_selected == "true", \
            f"Опція '{label}' не була вибрана після натискання 'Всі типи'"

    for label in ["Економічний", "Соціальний", "Екологічний"]:
        chip = page.get_chip(label)
        assert chip.is_displayed(), \
            f"Чіп '{label}' не з'явився після вибору 'Всі типи'"

    assert "Знайдено" in page.get_results_counter_text()