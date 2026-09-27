from Config.settings import Settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class WaitUtils:

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.timeout = timeout or Settings.DEFAULT_TIMEOUT
        self.wait = WebDriverWait(
            self.driver,
            self.timeout
        )

    def wait_for_visibility(self, locator):

        def visible(driver):
            try:
                element = driver.find_element(*locator)

                if element.is_displayed():
                    return element

                return False

            except StaleElementReferenceException:
                return False

        return self.wait.until(visible)

    def wait_for_clickable(self, locator):

        def clickable(driver):
            try:
                element = driver.find_element(*locator)

                if element.is_displayed() and element.is_enabled():
                    return element

                return False

            except StaleElementReferenceException:
                return False

        return self.wait.until(clickable)

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_url_contains(self, value):
        return self.wait.until(
            EC.url_contains(value)
        )