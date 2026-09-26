from Config.settings import Settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.timeout = timeout or Settings.DEFAULT_TIMEOUT
        self.wait = WebDriverWait(self.driver, self.timeout)

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

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