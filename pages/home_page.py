from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.header import HeaderComponent

class HomePage(BasePage):

    SEARCH_BOX = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(self.driver)

    def wait_until_loaded(self):
        self.wait.wait_for_visibility(self.SEARCH_BOX)

    def search_product(self, product_name):
        self.wait.wait_for_clickable(self.SEARCH_BOX)
        self.enter_text(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)

    def is_search_results_page(self):
        return "search" in self.driver.current_url.lower()