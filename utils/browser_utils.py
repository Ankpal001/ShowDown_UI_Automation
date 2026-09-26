class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver

    def maximize(self):
        self.driver.maximize_window()

    def fullscreen(self):
        self.driver.fullscreen_window()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_window_size(self):
        return self.driver.get_window_size()

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_current_url(self):
        return self.driver.current_url