from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-layout .caption h4")

    def is_product_displayed(self, product_name):
        products = self.wait.until(
            lambda driver: driver.find_elements(*self.PRODUCT_NAMES)
        )

        return any(
            product.text.strip().lower() == product_name.lower()
            for product in products
        )