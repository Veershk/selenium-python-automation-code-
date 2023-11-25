from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    register = (By.LINK_TEXT, "Register")

    def test_clickRegisterButton(self):
        return self.driver.find_element(*HomePage.register)