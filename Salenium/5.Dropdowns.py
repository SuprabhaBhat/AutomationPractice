import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.automationtesting.in/Register.html")
select_web = driver.find_element(By.ID, "Skills")
sel = Select(select_web)

#by index
sel.select_by_index(5)

#by value
#sel.select_by_value('Certifications')

#by visible text
#sel.select_by_visible_text('Design')
print(driver.current_url)

assert "Register" in driver.current_url

#browser commands
driver.get("https://google.com")
print(driver.current_url)
driver.refresh()
driver.back()
driver.forward()
driver.refresh()
driver.quit()