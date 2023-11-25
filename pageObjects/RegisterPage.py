from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    firstname = (By.ID, "firstName")
    lastname = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    phonenumber = (By.ID, "userMobile")
    occupation = (By.XPATH, "//select[@formcontrolname='occupation']")
    gender = (By.XPATH, "//input[@value='Male']")
    password = (By.ID, "userPassword")
    confirmpassword = (By.ID, "confirmPassword")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    registerbutton = (By.ID, "login")
    successmessage = (By.TAG_NAME, "h1")
    login = (By.XPATH, "//button[@class='btn btn-primary']")

    def test_entereFirstName(self):
        return self.driver.find_element(*RegisterPage.firstname)

    def test_enterLastName(self):
        return self.driver.find_element(*RegisterPage.lastname)

    def test_enterEmail(self):
        return self.driver.find_element(*RegisterPage.email)

    def test_enterPhoneNumber(self):
        return self.driver.find_element(*RegisterPage.phonenumber)

    def test_selectOccupation(self):
        return self.driver.find_element(*RegisterPage.occupation)

    def test_selectGender(self):
        return self.driver.find_element(*RegisterPage.gender)

    def test_enterPassword(self):
        return self.driver.find_element(*RegisterPage.password)

    def test_enterConfirmPassword(self):
        return self.driver.find_element(*RegisterPage.confirmpassword)

    def test_clickCheckbox(self):
        return self.driver.find_element(*RegisterPage.checkbox)

    def test_clickRegisterButton(self):
        return self.driver.find_element(*RegisterPage.registerbutton)

    def test_seeSuccessMessage(self):
        return self.driver.find_element(*RegisterPage.successmessage)

    def test_clickButton(self):
        return self.driver.find_element(*RegisterPage.login)
