from selenium.webdriver.common.alert import Alert


class AlertUtils:

    def __init__(self, driver):
        self.driver = driver

    def get_alert(self):
        return Alert(self.driver)

    def accept(self):
        self.get_alert().accept()

    def dismiss(self):
        self.get_alert().dismiss()

    def get_text(self):
        return self.get_alert().text

    def send_text(self, text):
        self.get_alert().send_keys(text)