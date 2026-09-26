from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value = 'Login']")
    LOGIN_ERROR = (By.CSS_SELECTOR, ".alert.alert-danger")
    ACCOUNT_HEADING = (By.XPATH, "//h2[normalize-space()='My Account']")

    def __init__(self, driver):
        super().__init__(driver)
    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR)

    def is_login_error_displayed(self):
        return self.is_displayed(self.LOGIN_ERROR)

    def is_login_successful(self):
        return self.is_displayed(self.ACCOUNT_HEADING)