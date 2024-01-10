import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.implicitly_wait(3)
driver.maximize_window()

sel_date="21-dec-2023"

dates = sel_date.split("-")
driver.find_element(By.XPATH,"//*[@class='imgdp']").click()
td = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//td")


for ele in td:
    if ele.text==dates[0]:
        ele.click()
        driver.implicitly_wait(5)
        break

