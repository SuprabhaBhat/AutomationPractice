import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.AddvendorPage import AddVendor
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_07_AddVendor:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_addVendor(self,setup):
        self.logger.info("************* Test_07_AddVendor **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting new Testcase to add vendor **********")
        self.addVend = AddVendor(self.driver)
        self.addVend.clickOnCustomersMenu()
        self.addVend.clickOnVendors()
        self.addVend.clickOnAddNewVendor()
        self.driver.implicitly_wait(10)

        self.logger.info("************* Providing customer vendor details **********")

        self.addVend.setName("Vendor 3")
        self.addVend.setDescription("Searching for opportunity..")
        self.email = random_generator() + "@gmail.com"
        self.addVend.setEmail(self.email)
        self.addVend.clickOnSave()

        self.logger.info("************* Saving vendor info **********")
        self.logger.info("********* Add vendor validation started *****************")

        self.msg = self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissable']").text

        print(self.msg)
        if 'Success' in self.msg:
            assert True
            self.logger.info("********* Vendor adding failed which is expected, Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_test.png")
            self.logger.error("********* Adding vendor failed, Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending,Thank you Universe **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))