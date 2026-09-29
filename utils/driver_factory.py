import os

from utils.drivers.chrome_strategy import ChromeStrategy
from utils.drivers.edge_strategy import EdgeStrategy
from utils.drivers.firefox_strategy import FirefoxStrategy


class DriverFactory:

    @staticmethod
    def create_driver(browser, headless=False):

        strategies = {
            "chrome": ChromeStrategy(),
            "firefox": FirefoxStrategy(),
            "edge": EdgeStrategy()
        }

        browser = browser.lower()

        if browser not in strategies:
            raise ValueError(f"Unsupported browser: {browser}")

        selenium_url = os.getenv("SELENIUM_URL")

        return strategies[browser].create_driver(
            headless=headless,
            selenium_url=selenium_url
        )