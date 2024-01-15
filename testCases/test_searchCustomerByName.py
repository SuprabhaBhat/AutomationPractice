import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_05_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* test_05_SearchCustomerByName **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.driver.implicitly_wait(10)
        self.addcust.clickOnCustomersMenu()
        time.sleep(10)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(10)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_05_SearchCustomerByName Finished!!!!!Hurray *********** ")

