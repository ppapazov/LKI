from pages.home.login_page import LoginPage
from utilities.teststatus import TStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):

        title = self.lp.verifyLoginTitle()
        self.ts.mark(title, "Title is OK")
        #self.lp.login("test@email.com", "abcabc")
        #result = self.lp.verifyLoginSuccessful()
        #self.ts.markFinal("test_validLogin", result, "Login is OK")

        #elf.lp.logout()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login()
        result = self.lp.verifyLoginFailed()
        assert result is True
