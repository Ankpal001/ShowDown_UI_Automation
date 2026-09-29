from selenium.common.exceptions import TimeoutException
from utils.retry_utils import RetryUtils
from utils.javascript_utils import JavaScriptUtils
from selenium.common.exceptions import ElementClickInterceptedException


class ElementUtils:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.js = JavaScriptUtils(driver)

    def click(self, locator):

        def action():
            element = self.wait.wait_for_clickable(locator)
            element.click()

        try:
            RetryUtils.execute(
                action,
                retries=3,
                delay=0.5
            )

        except ElementClickInterceptedException:
            element = self.wait.wait_for_clickable(locator)
            self.js.click_with_js(element)

    def enter_text(self, locator, value):

        def action():
            element = self.wait.wait_for_visibility(locator)
            element.clear()
            element.send_keys(value)

        RetryUtils.execute(
            action,
            retries=3,
            delay=0.5
        )

    def get_text(self, locator):
        return self.wait.wait_for_visibility(locator).text

    def is_displayed(self, locator):
        try:
            element = self.wait.wait_for_visibility(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def is_enabled(self, locator):
        element = self.wait.wait_for_visibility(locator)
        return element.is_enabled()

    def get_attribute(self, locator, attribute):
        element = self.wait.wait_for_visibility(locator)
        return element.get_attribute(attribute)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)