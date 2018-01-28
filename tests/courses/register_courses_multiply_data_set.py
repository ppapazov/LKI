from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TStatus
from base.selenium_driver import SeleniumDriver
import unittest
import pytest
from ddt import ddt, data, unpack
import  time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TStatus(self.driver)
        self.d = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "5457 0822 3591 3352", "12 / 19", "123", "01234"),
          ("Learn Python 3 from scratch", "5457 0822 3591 3352", "12 / 20", "123", "01234"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccDate, ccCvv, postal):
        self.courses.openCousesPage()
        self.courses.enterCourseName(courseName)
        self.courses.selectCoureToEnroll(courseName)
        self.courses.startEnroll()
        self.courses.enterEmail("s@yopmail.com")
        self.courses.enrollCource(num=ccNum, exp=ccDate, cvv=ccCvv, postal=postal)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed verification")
        self.driver.get("https://letskodeit.teachable.com")




