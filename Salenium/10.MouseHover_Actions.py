import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service_obj = Service("C:\Windows\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://magento.softwaretestingboard.com/")
driver.implicitly_wait(3)
driver.maximize_window()

Women = driver.find_element(By.XPATH,"//a[@id='ui-id-4']")
action = ActionChains(driver)
action.move_to_element(Women).perform()

Tops = driver.find_element(By.XPATH,"//a[@id='ui-id-9']")
action.move_to_element(Tops).perform()

Tees = driver.find_element(By.XPATH,"//a[@id='ui-id-13']")
action.click(Tees).perform()

time.sleep(3)

Search = driver.find_element(By.ID, "search")
action.click(Search).key_down(Keys.SHIFT).send_keys("Text").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()