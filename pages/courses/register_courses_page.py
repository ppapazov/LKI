import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"
    _course = "//a[@href='/p/complete-javascript-guide']"
    _all_courses = "presentation"
    _enroll_button = "enroll-button-top"
    _use_another_card = "Use another card"
    _cc_num = "cardnumber"
    _cc_expired = "exp-date"
    _cc_cvv = "cvc"
    _cc_postal = "postal"
    _submit_enroll = "confirm-purchase"
    _enroll_error_message = "//div[.='The card number is incorrect.']"
    _courses = "//a[@href='/courses']"
    _email = "email"


    def openCousesPage(self):
        self.elementClick(self._courses, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)

    def selectCoureToEnroll(self):
        self.elementClick(self._course, locatorType="xpath")

    def startEnroll(self):
        self.elementClick(self._enroll_button)

    def enterEmail(self, email):
        self.sendKeys(email, self._email)

    def enterCardNum(self, num):
        self.driver.switch_to.frame("__privateStripeFrame3")
        self.sendKeys(num, self._cc_num, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.driver.switch_to.frame("__privateStripeFrame4")
        self.sendKeys(exp, self._cc_expired, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        self.driver.switch_to.frame("__privateStripeFrame5")
        self.sendKeys(cvv, self._cc_cvv, locatorType="name")
        self.driver.switch_to.default_content()

    def enterPostal(self, postal):
        self.driver.switch_to.frame("__privateStripeFrame6")
        self.sendKeys(postal, self._cc_postal, locatorType="name")
        self.driver.switch_to.default_content()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll)

    def enterCreditCardData(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardCVV(cvv)
        self.enterCardExp(exp)

    def enrollCource(self, num="", exp="", cvv=""):
        self.enterCreditCardData(num="5457 0822 3591 3352", exp="‎12 / ‎19", cvv="123")
        self.enterPostal(postal="1")
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        self.isElementDisplayed(self._enroll_error_message, locatorType="xpath")


