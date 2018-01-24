from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TStatus
from base.selenium_driver import SeleniumDriver
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_file import getCSVdata
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TStatus(self.driver)
        self.d = SeleniumDriver(self.driver)

    def setUp(self):
        self.driver.get("https://letskodeit.teachable.com")

    @pytest.mark.run(order=1)
    @data(*getCSVdata("/Users/pavelpapazov/PycharmProjects/LetsKodeit/test_data.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccDate, ccCvv, postal):
        self.courses.openCousesPage()
        self.courses.enterCourseName(courseName)
        self.courses.selectCoureToEnroll(courseName)
        self.courses.startEnroll()
        self.courses.enterEmail("s@yopmail.com")
        time.sleep(1)
        self.courses.enrollCource(num=ccNum, exp=ccDate, cvv=ccCvv, postal=postal)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed verification")





