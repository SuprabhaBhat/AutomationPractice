import time

# contains
# //label[contains(text(),'Full Name')]
# text
# //label[text()='Full Name*']
# index
# //label[2]
# and , or: to match both or either condition
# //input[@placeholder="First Name" and @ng-model="FirstName"]
#
# child -parent:
# //form[@id="basicBootstrapForm"]/child::div
# parent -child
# //form[@id="basicBootstrapForm"]/parent::div
# From ancestor
# //form[@id="basicBootstrapForm"]/ancestor::div
# Following- sibling- preceding
# //input[@id='checkbox1']//following-siblibg::label
# //input[@id='checkbox1']//preceding-siblibg::label

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Suprabha")
driver.find_element(By.XPATH,"//*[@placeholder='Last Name']").send_keys("Bhat")
