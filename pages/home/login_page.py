import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_filed = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self._password_filed)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")



    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def verifyLoginSuccessful(self):
        elementPresent = self.isElementPresent("//div[@id='navbar']//span[text()='User Settings']",
                                               locatorType="xpath")
        return elementPresent

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains (text(),'Invalid email or password')]", locatorType="xpath")

        return result

    # def logout(self):
    #     self.elementClick("//li[@class='dropdown']", locatorType="xpath")
    #     self.elementClick("//a[@href='/sign_out']", locatorType="xpath")

    def verifyLoginTitle(self):
        self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettingIcon()
        self.elementClick("//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath")


