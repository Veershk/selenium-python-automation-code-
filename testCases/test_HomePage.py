import time

from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import RegisterPage
from utilities.BaseClass import BaseClass


class TestRahulShettyAcademy(BaseClass):
    def test_verifyHomepageTitle(self):
        actualtitle = self.driver.title
        expectedtitle = "Let's Shop"
        if actualtitle == expectedtitle:
            print("Lets Shop page is opened")
            log.info("Home Page title is correct")
        else:
            print("Lets Shop page is not opened")
            log.info("Home Page title is not correct")

    def test_clickButtonRegister(self):
        hp = HomePage(self.driver)
        hp.test_clickRegisterButton().click()

    def test_RegistationPageRegisterButton(self):
        rpg = RegisterPage(self.driver)
        rpg.test_clickRegisterButton().click()
        self.driver.get_screenshot_as_file("..//Screenshots//test_RegistationPageRegisterButton.png")
        time.sleep(2)

    def test_pageRegistration(self):
        rp = RegisterPage(self.driver)
        rp.test_entereFirstName().send_keys("Ankit")
        rp.test_enterLastName().send_keys("Solanki")
        rp.test_enterEmail().send_keys("109@gmail.com")
        rp.test_enterPhoneNumber().send_keys("1234567890")
        occupation = Select(rp.test_selectOccupation())
        occupation.select_by_visible_text("Engineer")
        rp.test_selectGender().click()
        rp.test_enterPassword().send_keys("June30@#$")
        rp.test_enterConfirmPassword().send_keys("June30@#$")
        rp.test_clickCheckbox().click()
        rp.test_clickRegisterButton().click()
        self.driver.get_screenshot_as_file("..//Screenshots//test_pageRegistration.png")
        msg = rp.test_seeSuccessMessage().text
        print(msg)
        time.sleep(2)
        rp.test_clickButton().click()
        self.driver.save_screenshot("..//Screenshots//test_pageRegitrationfailed.png")

    def test_enterCredentials(self):
        lp = LoginPage(self.driver)
        lp.test_enterEmail().send_keys("109@gmail.com")
        lp.test_enterPassword().send_keys("June30@#$")
        time.sleep(2)
        lp.test_clickLoginButton().click()

