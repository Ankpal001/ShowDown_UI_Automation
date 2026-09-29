from time import sleep

from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementNotInteractableException,
    ElementClickInterceptedException
)

from Config.settings import Settings


class RetryUtils:

    @staticmethod
    def execute(
        action,
        retries=None,
        delay=None,
        exceptions=(
            StaleElementReferenceException,
            ElementNotInteractableException,
            ElementClickInterceptedException
        )
    ):
        retries = retries if retries is not None else Settings.DEFAULT_RETRIES
        delay = delay if delay is not None else Settings.RETRY_DELAY

        last_exception = None

        for attempt in range(retries):
            try:
                return action()

            except exceptions as e:
                last_exception = e

                if attempt < retries - 1:
                    sleep(delay)

        raise last_exception