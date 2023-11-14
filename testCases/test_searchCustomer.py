from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.searchCustomerPage import searchCustomer
from pageObjects.AddcustomerPage import AddCustomer
import time


class Test_004_SearchCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_verifySearch_Customer_ByEmail(self, setUp):
        self.logger.info("*****Test_003_SearchCustomerByEmail*****")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****Login Successful*****")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.logger.info("*****Search Customer Page Displayed*****")
        self.logger.info("*****Providing Customer Email*****")

        self.sC = searchCustomer(self.driver)
        self.sC.setSearchEmail("victoria_victoria@nopCommerce.com")
        self.sC.setclickOnSearchBtn()
        self.logger.info("*****Customer searched by Email Completed*****")
        self.logger.info("*****Start Search Validation*****")
        time.sleep(3)

        self.result = self.driver.find_element("xpath", "/td[contains(text(),'victoria_victoria@nopCommerce.com')]").text
        if "victoria_victoria@nopCommerce.com" in self.result:
            self.logger.info("*****Search Customer Test Passed*****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchCustByEmail.png")
            self.logger.error("*****Search Customer Test Failed*****")
            assert False
        self.logger.info("*****Search Customer Test Completed*****")
