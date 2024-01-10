import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/")

driver.find_element(By.LINK_TEXT,"About").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"How").click()
time.sleep(2)