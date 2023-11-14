class searchCustomer:
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstname_xpath = "//input[@id='SearchFirstName']"
    txtLastname_xpath = "//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"

    tblSearchresult_xpath = "//div[@id='customers-grid_wrapper']"
    table_xpath = "//table[@id='customers-grid']"
    tablerow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setSearchEmail(self, email):
        self.driver.find_element("xpath", self.txtEmail_xpath).clear()
        self.driver.find_element("xpath", self.txtEmail_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element("xpath", self.txtFirstname_xpath).clear()
        self.driver.find_element("xpath", self.txtFirstname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element("xpath", self.txtLastname_xpath).clear()
        self.driver.find_element("xpath", self.txtLastname_xpath).send_keys(lname)

    def setclickOnSearchBtn(self):
        self.driver.find_element("xpath", self.btnSearch_xpath).click()

    def getNoOfRow(self):
        return len(self.driver.find_element("xpath", self.tablerow_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element("xpath", self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1,self.getNoOfRow()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            emailid = table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]")
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1,self.getNoOfRow()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            name = table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]")
            if name == Name:
                flag = True
                break
        return flag

