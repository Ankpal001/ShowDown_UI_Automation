from selenium import webdriver
from utils.drivers.browser_strategy import BrowserStrategy


class EdgeStrategy(BrowserStrategy):

    def create_driver(self, headless=False):
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-notifications")

        if headless:
            options.add_argument("--headless")

        return webdriver.Edge(options=options)