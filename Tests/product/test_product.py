import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.regression
def test_search_product(driver, base_url, login_data, test_password):
    data = login_data["valid_user"]

    login_page = LoginPage(driver)
    login_page.navigate_to(base_url)
    login_page.login(data["username"], test_password)

    home_page = HomePage(driver)
    home_page.search_product("MacBook")

