import pytest
from Config import config
from utils.driver_factory import DriverFactory
from utils.test_data_reader import TestDataReader
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store",
    default = "chrome",help = "browser to run test")
    parser.addoption("--headless",action="store_true",
        default=False,
        help="Run browser in headless mode"
    )
    parser.addoption("--env", action="store",
    default="qa",
    help="Environment to run tests against"
)
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.create_driver(browser = browser, headless = headless)
    yield driver
    driver.quit()

@pytest.fixture
def environment(request):
    env =  request.config.getoption("--env")
    if env not in config.ENVIRONMENTS:
        raise ValueError(
            f"Unsupported environment: {env}"
        )

    return config.ENVIRONMENTS[env]

@pytest.fixture
def base_url(environment):
    return environment["base_url"]

@pytest.fixture
def login_data():
    return TestDataReader.read_json("test_data/login_data.json")

import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            worker_id = os.environ.get("PYTEST_XDIST_WORKER", "master")

            screenshot_name = (
                f"screenshots/{worker_id}_{item.name}.png"
            )

            driver.save_screenshot(screenshot_name)

            print(
                f"\nScreenshot saved: {screenshot_name}"
            )
            with open(screenshot_name, "rb") as image_file:
                allure.attach(
                    image_file.read(),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

@pytest.fixture
def test_password():
    return os.getenv("TEST_PASSWORD")