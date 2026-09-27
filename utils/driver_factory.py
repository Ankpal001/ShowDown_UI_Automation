import os
from selenium import webdriver


class DriverFactory:

    @staticmethod
    def create_driver(browser, headless=False):

        browser = browser.lower()

        selenium_url = os.getenv("SELENIUM_URL")

        # =========================
        # Remote / Selenium Grid
        # =========================

        if selenium_url:

            if browser == "chrome":

                options = webdriver.ChromeOptions()
                options.add_argument("--disable-notifications")

                if headless:
                    options.add_argument("--headless")

                return webdriver.Remote(
                    command_executor=selenium_url,
                    options=options
                )

            elif browser == "firefox":

                options = webdriver.FirefoxOptions()

                if headless:
                    options.add_argument("--headless")

                return webdriver.Remote(
                    command_executor=selenium_url,
                    options=options
                )

            elif browser == "edge":

                options = webdriver.EdgeOptions()
                options.add_argument("--disable-notifications")

                if headless:
                    options.add_argument("--headless")

                return webdriver.Remote(
                    command_executor=selenium_url,
                    options=options
                )

            else:
                raise ValueError(
                    f"Unsupported remote browser: {browser}"
                )

        # =========================
        # Local execution
        # =========================

        if browser == "chrome":

            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

        elif browser == "edge":

            options = webdriver.EdgeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        return driver