

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class EventsPage:
    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # --- Locators ---
    FILTER_BUTTON = (
        By.XPATH,
        "//mat-label[contains(text(), 'Тип події')]"
        "/following-sibling::mat-select",
    )
    MAT_OPTION = (By.CSS_SELECTOR, "mat-option")
    OVERLAY_BACKDROP = (By.CSS_SELECTOR, ".cdk-overlay-backdrop-showing")

    OPTION_ECONOMIC = (By.XPATH, "//mat-option[contains(.,'Економічний')]")
    OPTION_SOCIAL   = (By.XPATH, "//mat-option[contains(.,'Соціальний')]")
    OPTION_ECOLOGY  = (By.XPATH, "//mat-option[contains(.,'Екологічний')]")
    OPTION_ALL      = (By.XPATH, "//mat-option[contains(.,'Всі типи')]")

    RESULTS_COUNTER = (By.XPATH, "//*[contains(text(),'Знайдено')]")

    def __init__(self, driver, timeout: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def open_type_filter(self):
        trigger = self.wait.until(EC.element_to_be_clickable(self.FILTER_BUTTON))
        self.driver.execute_script("arguments[0].click();", trigger)
        self.wait.until(EC.presence_of_element_located(self.MAT_OPTION))

    def close_type_filter(self):
        """Закриває дропдаун повторним кліком на кнопку фільтру."""
        btn = self.wait.until(EC.element_to_be_clickable(self.FILTER_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)

    def select_option(self, locator: tuple):
        option = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
        self.driver.execute_script("arguments[0].click();", option)

    def is_option_selected(self, locator: tuple) -> bool:
        option = self.wait.until(EC.presence_of_element_located(locator))
        return option.get_attribute("aria-selected") == "true"

    def get_filter_chip(self, label: str):
        locator = (
            By.XPATH,
            f"//*[contains(text(),'{label}') and "
            f"(contains(@class,'chip') or contains(@class,'tag') or "
            f"ancestor::*[contains(@class,'filter')])]",
        )
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_filter_chip_visible_by_default(self, label: str):
        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(self.driver, 3).unti(
                EC.visibility_of_element_located((By.XPATH, f"//[*contains(text(), '{label}') and "
                                                  f"(contains(@class, 'chip') or contains(@class, 'tag') or "
                                                  f"ancestor::*[contains(@class, 'filter')])]"
                                                  ))
            )
            return True
        except TimeoutException:
            return False
    def get_option_aria_selected(self, locator: tuple) -> str:
        option = self.wait.until(EC.presence_of_element_located(locator))
        return option.get_attribute("aria-selected")
    def is_filter_chip_visible(self, label: str) -> bool:
        return self.get_filter_chip(label).is_displayed()

    def get_results_counter_text(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(self.RESULTS_COUNTER))
        return el.text

    def is_overlay_closed(self) -> bool:
        return self.wait.until(
            EC.invisibility_of_element_located(self.OVERLAY_BACKDROP)
        )

    def escape_dropdown(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)