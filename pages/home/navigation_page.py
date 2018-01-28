import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "//a[@href='/courses/enrolled']"
    _courses = "//a[@href='/courses']"
    _practice = "//a[@href='/pages/practice']"
    _user_settings_icon = "//div[@id='navbar']//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown']/a"
    _main_page = "//a/img"

    def navigateToAllCourses(self):
        self.elementClick(self._courses, locatorType="xpath")
        time.sleep(1)


    def navigateToMyCourses(self):
        self.elementClick(self._my_courses, locatorType="xpath")

    def navigateToPractice(self):
        self.elementClick(self._practice, locatorType="xpath")

    def navigateToUserSettingIcon(self):
        self.elementClick(self._user_settings_icon, locatorType="xpath")

    def navigateToMainPage(self):
        self.elementClick(self._main_page, locatorType="xpath")
        time.sleep(1)

