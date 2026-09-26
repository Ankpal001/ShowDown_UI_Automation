from utils.retry_utils_learn import RetryUtils


class ElementUtils:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click(self, locator):
        def action():
            element = self.wait.wait_for_clickable(locator)
            element.click()

        RetryUtils.execute(
            action,
            retries=3,
            delay=0.5
        )

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
        return self.wait.wait_for_visibility(locator).is_displayed()

    def is_enabled(self, locator):
        return self.wait.wait_for_visibility(locator).is_enabled()

    def get_attribute(self, locator, attribute):
        return self.wait.wait_for_visibility(locator).get_attribute(attribute)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)