import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def make_driver() -> webdriver.Chrome:
    """Factory used by every test setUp."""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # uncomment for CI
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver