import os
from selenium import webdriver
from utils.drivers.browser_strategy import BrowserStrategy


class ChromeStrategy(BrowserStrategy):

    def create_driver(self, headless=False, selenium_url=None):

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")

        if not selenium_url:
            options.add_argument("--start-maximized")

        if headless:
            options.add_argument("--headless")

        if selenium_url:
            return webdriver.Remote(
                command_executor=selenium_url,
                options=options
            )

        return webdriver.Chrome(options=options)