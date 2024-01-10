from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.automationtesting.in/Index.html")

driver.find_element(By.ID,"email").send_keys("suppi@gmail.com")
driver.find_element(By.ID,"enterimg").click()