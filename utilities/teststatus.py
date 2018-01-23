import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class TStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TStatus, self).__init__(driver)
        self.resultsList = []

    def setResults(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultsList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultsList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultsList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultsList.append("FAIL")
            self.log.info("### Exception Occurred !!!")
            self.screenShot(resultMessage   )

    def mark(self, result, resultMessage):
        self.setResults(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResults(result, resultMessage)
        if "FAIL" in self.resultsList:
            self.log.info(testName + " ### TEST FAILED !!!")
            self.resultsList.clear()
            assert True is False
        else:
            self.log.info(testName + " TEST SUCCESSFUL")
            self.resultsList.clear()
            assert True is True


