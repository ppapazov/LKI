from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def GetWebdriverInstance(self):

        baseUrl = "https://letskodeit.teachable.com"
        if self.browser == "iexplorer":
           driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
