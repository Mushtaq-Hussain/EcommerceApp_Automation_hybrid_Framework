# ********To run tests on desired browser***************

# pytest -s -v testCases/test_Login.py --default Edge browser
# pytest -s -v testCases/test_Login.py --browser chrome
# pytest -s -v testCases/test_Login.py --browser firefox

# *********To run tests Parallel***********************

# pytest -s -v -n=2 testCases/test_Login.py --browser chrome
# pytest -s -v -n=2 testCases/test_Login.py --browser firefox
# ****************HTML Reports***********************************
# pytest -n=2 --html=Reports/report.html testCases/test_Login.p
# y --browser chrome

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_LoginPage:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_verifyTitle(self, setUp):
        self.logger.info("******Test_001_Login*****")
        self.logger.info("******Verifying Home Page title*****")
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.logger.info("******Browser opened*****")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******Verifying Title of home page test case is passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_verifyTitle.png")
            self.driver.close()
            self.logger.error("******Verifying Title of home page test case is Failed*****")
            assert False

    def test_login_with_valid_credentials(self, setUp):
        self.logger.info("******Verifying login with valid credentials*****")
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.logger.info("******Browser opened*****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.lp.clickLogOut()
            self.driver.close()
            self.logger.info("******Verifying Login test case is Passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_with_valid_credentials.png")
            self.driver.close()
            self.logger.error("******Verifying Login test case is Failed*****")
            assert False
