import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddVendor:

    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkVendor_xpath = "//p[normalize-space()='Vendors']"
    btnAddNewVendor_xpath = "//a[normalize-space()='Add new']"

    txtName_xpath = "//input[@id='Name']"
    txtEmail_xpath = "//input[@id='Email']"
    txtDescription_xpath = "//iframe[@id='Description_ifr']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]"))).click()

    def clickOnVendors(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,self.lnkVendor_xpath))).click()

    def clickOnAddNewVendor(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,self.btnAddNewVendor_xpath))).click()

    def setName(self, name):
        self.driver.find_element(By.XPATH,self.txtName_xpath).send_keys(name)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setDescription(self, content):
        iframe = self.driver.find_element(By.XPATH,self.txtDescription_xpath).send_keys(content)
        self.driver.switch_to.frame(iframe)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
