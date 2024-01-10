import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Frames.html")

#using index
#driver.switch_to.frame(0)

#using name or id
#driver.switch_to.frame("singleframe")  #id
#driver.switch_to.frame("SingleFrame")  #name

#using web element
single_frame = driver.find_element(By.XPATH,"//div[@id='Single']/iframe")
driver.switch_to.frame(single_frame)

driver.find_element(By.TAG_NAME,'Input').send_keys("This is text box")
time.sleep(2)

#return to home default
#driver.switch_to.default_content()