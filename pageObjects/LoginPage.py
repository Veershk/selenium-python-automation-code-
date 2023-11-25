from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    email = (By.ID, "userEmail")
    password = (By.ID, "userPassword")
    loginbutton = (By.ID, "login")

    def test_enterEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def test_enterPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def test_clickLoginButton(self):
        return self.driver.find_element(*LoginPage.loginbutton)

