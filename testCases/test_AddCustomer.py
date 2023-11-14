# pytest --html=Reports/report.html testCases/test_AddCustomer.py --browser chrome

import random
import string

from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_Verify_Add_New_Customer(self, setUp):
        self.logger.info("*****Test_003_AddCustomer*****")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*********Login Successful*********")
        self.logger.info("*********Starting Add customer test*********")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddnew()
        self.addCust.setinfobtn()
        self.logger.info("*********Providing Customer info*********")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Mushtaq")
        self.addCust.setLastName("Hussain")
        self.addCust.setGender("Male")
        self.addCust.setDob("08/05/1995")
        self.addCust.setCompanyName("Testing Gurus")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminContent("This for testing.......")
        self.addCust.clickOnSave()

        self.logger.info("*********Saving Customer info*********")
        self.logger.info("*********Validating Customer info*********")

        self.msg = self.driver.find_element("xpath", "//body/div[3]/div[1]/div[1]").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*********Add Customer Test Passed*********")
        else:
            self.driver.save_screenshot(".\\Screentshots\\" + "test_AddCostumer_screenshot.png")
            assert True == False
            self.logger.error("*********Add Customer Test Failed*********")
        self.driver.close()
        self.logger.info("*********Ending Add Customer Test*********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
