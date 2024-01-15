import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.AddcustomerRole import AddCustomerRoles
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_06_AddCustomerRole:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomerRole(self,setup):
        self.logger.info("************* Test_06_AddCustomer Role **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting new Testcase to add **********")
        self.addrole = AddCustomerRoles(self.driver)
        self.addrole.clickOnCustomersMenu()
        self.addrole.clickOnCustomersRole()
        self.driver.implicitly_wait(10)
        self.addrole.clickOnAddNewRole()
        self.driver.implicitly_wait(10)

        self.logger.info("******** Providing customer role details *******")

        self.addrole.setName("Suprabha bhat")
        self.addrole.clickOnFreeShipping()
        self.addrole.clickOnTaxExempt()
        self.addrole.clickOnEnablePass()
        self.addrole.setSystemyName("mytsl06234")
        self.addrole.clickOnSave()

        self.logger.info("************* Saving customer role info **********")
        self.logger.info("********* Add customer role validation started *****************")

        self.msg = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text

        print(self.msg)
        if 'customer role has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Customer role added, Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomerRole_test.png")
            self.logger.error("********* Adding customer role failed, Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending,Thank you Universe **********")

