import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://demo.automationtesting.in")
driver.find_element(By.ID,"email").send_keys("test@gmail.com")
driver.find_element(By.ID,"enterimg").click()


#wait sleep
#time.sleep(2)

#implicit - waits until all condition matched /
#driver.implicitly_wait(5)

#explicit
wait = WebDriverWait(driver,5)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='First Name']"))).send_keys("Suprabha")


