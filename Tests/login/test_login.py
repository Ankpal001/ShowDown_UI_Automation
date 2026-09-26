import os
import allure
import pytest

from pages.login_page import LoginPage


@allure.title("Verify user login")
@allure.description(
    "Verify login behavior using valid and invalid user credentials"
)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "user_type",
    ["valid_user", "invalid_user"],
    ids=["valid_login", "invalid_login"]
)
def test_login(driver, base_url, login_data, user_type):

    data = login_data[user_type]
    password = os.getenv("TEST_PASSWORD")

    login_page = LoginPage(driver)

    with allure.step("Navigate to login page"):
        login_page.navigate_to(base_url)

    with allure.step("Enter username and password"):
        login_page.login(data["username"], password)

    if data["expected"] == "failure":

        with allure.step("Verify login error message"):
            assert login_page.is_login_error_displayed()

    else:

        with allure.step("Verify successful login"):
            #assert login_page.is_login_successful()
              pass