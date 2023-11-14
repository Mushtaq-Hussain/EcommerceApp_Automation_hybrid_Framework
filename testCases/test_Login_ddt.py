# pytest --html=Reports/report.html testCases/test_Login_ddt.py --browser chrome

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplicationUrl()
    logger = LogGen.logGen()
    path = ".//TestData/LoginData.xlsx"

    def test_login_with_valid_credentials(self, setUp):
        self.logger.info("******Test_002_DDT_Login*****")
        self.logger.info("******Verifying DDT Login Test Case*****")
        self.driver = setUp
        self.driver.get(self.baseurl)
        self.logger.info("******Browser opened*****")
        self.lp = LoginPage(self.driver)
        self.row = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of rows in a Excel: ", self.row)
        lst_status = []
        for r in range(2, self.row + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Test Case is passed")
                    self.lp.clickLogOut()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("Test Case is Failed")
                    self.lp.clickLogOut()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Test Case is Failed")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Test Case is passed")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test Case is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test Case is Failed")
            self.driver.close()
            assert False
        self.logger.info("End of Login DDT Test")
        self.logger.info("Complete TC_Login_DDT_002")
