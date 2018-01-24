from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TStatus
from base.selenium_driver import SeleniumDriver
import unittest
import pytest


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
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCoureToEnroll("JavaScript for beginners")
        self.courses.startEnroll()
        self.courses.enterEmail("s@yopmail.com")
        self.d.scrollPage(direction="down")
        self.courses.enrollCource(num="5457 0822 3591 3352", exp="12 / 19", cvv="123", postal="01234")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed verification")




