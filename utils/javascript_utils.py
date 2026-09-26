class JavaScriptUtils:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def scroll_to_top(self):
        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def click_with_js(self, element):
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def set_value(self, element, value):
        self.driver.execute_script(
            "arguments[0].value = arguments[1];",
            element,
            value
        )

    def highlight_element(self, element):
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red';",
            element
        )