from utils.wait_utils import WaitUtils
from utils.element_utils import ElementUtils
from utils.logger import Logger
from utils.browser_utils import BrowserUtils
from utils.alert_utils import AlertUtils

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.element = ElementUtils(driver, self.wait)
        self.logger = Logger.get_logger(self.__class__.__name__)
        self.browser = BrowserUtils(self.driver)
        self.alert = AlertUtils(self.driver)

    def navigate_to(self, url):
        self.logger.info(f"Navigating to {url}")
        self.driver.get(url)

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.element.click(locator)

    def enter_text(self, locator, value):
        self.logger.info(f"Entering text into: {locator}")
        self.element.enter_text(locator, value)

    def get_text(self, locator):
        self.logger.info(f"Getting text from: {locator}")
        return self.element.get_text(locator)

    def is_displayed(self, locator):
        return self.element.is_displayed(locator)