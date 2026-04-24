import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.events_page import EventsPage


class BaseTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.page = EventsPage(self.driver)
        self.page.open()

    def tearDown(self):
        if self.driver:
            self.driver.quit()