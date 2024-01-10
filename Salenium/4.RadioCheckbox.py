import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Suprabha")
driver.find_element(By.XPATH,"//*[@placeholder='Last Name']").send_keys("Bhat")
driver.find_element(By.XPATH,"//input[@value='FeMale']").click()

li = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for ele in li:
    val = ele.get_attribute('value')
    print(val)
    if val == 'Cricket':
        ele.click()
        time.sleep(2)
