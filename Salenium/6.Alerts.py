import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Alerts.html")
#ok- accept
driver.find_element(By.ID,"OKTab").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

#confirmation
driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()
driver.find_element(By.ID,"CancelTab").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

#Read text and enter text
driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()
driver.find_element(By.ID,"Textbox").click()
tx = driver.switch_to.alert.text
print(tx)
assert tx in "Please enter your name"
driver.switch_to.alert.send_keys("suprabha")
driver.switch_to.alert.accept()
time.sleep(2)

#driver.switch_to.alert.dismiss()
#time.sleep(2)

driver.quit()