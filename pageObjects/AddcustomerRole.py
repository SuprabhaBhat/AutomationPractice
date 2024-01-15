import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomerRoles:

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_role_xpath = "(//p[normalize-space()='Customer roles'])[1]"
    btnAddNewRole_xpath = "(//a[normalize-space()='Add new'])[1]"

    txtName_xpath = "//input[@id='Name']"
    Tax_exempt_xpath = "//input[@id='TaxExempt']"
    FreeShipping_xpath = "//input[@id='FreeShipping']"
    EnablePass_xpath = "//input[@id='EnablePasswordLifetime']"
    txtSystemName_xpath = "//input[@id='SystemName']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersRole(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_role_xpath).click()

    def clickOnAddNewRole(self):
        self.driver.find_element(By.XPATH,self.btnAddNewRole_xpath).click()

    def setName(self,name):
        self.driver.find_element(By.XPATH,self.txtName_xpath).send_keys(name)

    def clickOnFreeShipping(self):
        self.driver.find_element(By.XPATH,self.FreeShipping_xpath).click()

    def clickOnTaxExempt(self):
        self.driver.find_element(By.XPATH,self.Tax_exempt_xpath).click()

    def clickOnEnablePass(self):
        self.driver.find_element(By.XPATH, self.EnablePass_xpath).click()

    def setSystemyName(self,name):
        self.driver.find_element(By.XPATH,self.txtSystemName_xpath).send_keys(name)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
