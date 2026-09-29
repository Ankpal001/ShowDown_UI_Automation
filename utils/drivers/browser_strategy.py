from abc import ABC, abstractmethod


class BrowserStrategy(ABC):

    @abstractmethod
    def create_driver(self, headless=False, selenium_url=None):
        pass