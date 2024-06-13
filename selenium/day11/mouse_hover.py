from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

elem_1 = driver.find_element(By.XPATH, "//span[text()='Courses']")
elem_2 = driver.find_element(By.XPATH, "//span[text()='For Working Professionals']")
elem_3 = driver.find_element(By.XPATH, "//a[text()='DevOps Engineering (LIVE)']")

act_obj=ActionChains(driver)
act_obj.move_to_element(elem_1).perform()
act_obj.move_to_element(elem_2).perform()
act_obj.move_to_element(elem_3).perform()
elem_3.click()

print(driver.title)