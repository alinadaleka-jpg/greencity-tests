import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class EventsPage(BasePage):

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    TYPE_FILTER_BUTTON = (
        By.XPATH,
        "//*[contains(text(),'Тип події') and (self::button or @role='button' "
        "or ancestor::button or ancestor::*[@role='button'])]"
    )
    MAT_OPTION_ANY = (By.CSS_SELECTOR, "mat-option")
    ECONOMIC_OPTION = (By.XPATH, "//mat-option[contains(.,'Економічний')]")
    SELECT_ALL_OPTION = (By.XPATH, "//mat-option[contains(.,'Всі типи')]")
    OVERLAY_BACKDROP = (By.CSS_SELECTOR, ".cdk-overlay-backdrop-showing")
    RESULTS_COUNTER = (By.XPATH, "//*[contains(text(),'Знайдено')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.place-input")
    CATEGORY_OPTIONS = (
        By.XPATH,
        "//mat-option[contains(.,'Економічний') or "
        "contains(.,'Соціальний') or "
        "contains(.,'Екологічний')]"
    )

    @staticmethod
    def chip_locator(label: str) -> tuple:
        return (
            By.XPATH,
            f"//*[contains(text(),'{label}') and "
            f"(contains(@class,'chip') or contains(@class,'tag') or "
            f"ancestor::*[contains(@class,'filter')])]"
        )

    def open(self) -> "EventsPage":
        self.driver.get(self.URL)
        return self

    def open_type_filter(self) -> "EventsPage":
        button = self.wait_for_clickable(self.TYPE_FILTER_BUTTON)
        self.js_click(button)
        self.wait_for_presence(self.MAT_OPTION_ANY)
        time.sleep(0.8)
        return self

    def select_option(self, locator: tuple) -> "EventsPage":
        option = self.wait_for_presence(locator)
        self.js_scroll_and_click(option)
        return self

    def select_economic_filter(self) -> "EventsPage":
        return self.select_option(self.ECONOMIC_OPTION)

    def select_all_types(self) -> "EventsPage":
        self.select_option(self.SELECT_ALL_OPTION)
        time.sleep(1.0)
        return self

    def close_filter_with_second_click(self) -> "EventsPage":
        button = self.wait_for_clickable(self.TYPE_FILTER_BUTTON)
        self.js_click(button)
        self.wait_for_presence(self.OVERLAY_BACKDROP)
        time.sleep(0.5)
        self.js_click(button)
        return self

    def is_dropdown_closed(self) -> bool:
        return self.wait_for_invisibility(self.OVERLAY_BACKDROP)

    def get_chip(self, label: str):
        return self.wait_for_visibility(self.chip_locator(label))

    def get_results_counter_text(self) -> str:
        return self.wait_for_visibility(self.RESULTS_COUNTER).text

    def get_category_options(self) -> list:
        return self.find_elements(self.CATEGORY_OPTIONS)

    def search(self, query: str) -> "EventsPage":
        field = self.wait_for_presence(self.SEARCH_INPUT)
        field.clear()
        field.send_keys(query)
        field.send_keys(Keys.ENTER)
        time.sleep(1.5)
        return self

    def clear_search(self) -> "EventsPage":
        field = self.wait_for_presence(self.SEARCH_INPUT)
        field.clear()
        field.send_keys(Keys.ENTER)
        time.sleep(1.0)
        return self