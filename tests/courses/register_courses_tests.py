from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TStatus
from  base.selenium_driver import SeleniumDriver
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TStatus(self.driver)
        self.d = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.openCousesPage()
        self.courses.enterCourseName("javaScript for beginners")
        self.courses.selectCoureToEnroll()
        self.courses.startEnroll()
        self.courses.enterEmail("s@yopmail.com")
        self.d.scrollPage(direction="down")
        self.courses.enrollCource()
        # self.courses.enterCardNum("5457 0822 3591 3352")
        # time.sleep(2)
        # self.courses.enterCardCVV("123")
        # time.sleep(2)
        # self.courses.enterCardExp("12/19")
        # time.sleep(2)
        # self.courses.enterPostal("01032")
        # time.sleep(2)
        # self.courses.clickEnrollSubmitButton()
        time.sleep(5)
        self.courses.verifyEnrollFailed()




