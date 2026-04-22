from pages.events_page import EventsPage


def test_tc2_filter_by_economic_type(driver):
    """TC-2: Перевірка вибору категорії фільтрації 'Економічний'"""
    page = EventsPage(driver).open()

    page.open_type_filter()
    page.select_economic_filter()

    chip = page.get_chip("Економічний")
    assert chip.is_displayed(), \
        "Фільтр 'Економічний' не був застосований або тег не з'явився."

    assert "Знайдено" in page.get_results_counter_text()