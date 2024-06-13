from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Explore Community')]").click()

# driver.close()
driver.quit()
sleep(10)