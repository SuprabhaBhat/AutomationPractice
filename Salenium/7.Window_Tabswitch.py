import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

#parent window
parent = driver.current_window_handle
print(parent)
time.sleep(2)
#driver.find_element(By.XPATH,"//a[@href='#Tabbed']").click()
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()

#all window
windows = driver.window_handles
time.sleep(2)

#switch to child window
for window in windows:
    if window != parent:
        driver.switch_to.window(window)
    #print(window)
time.sleep(2)

#actions in child window
driver.find_element(By.XPATH,"//span[contains(text(),'Downloads')]").click()
time.sleep(2)
driver.close()
time.sleep(2)
driver.switch_to.window(parent)
driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()
time.sleep(2)
driver.quit()



