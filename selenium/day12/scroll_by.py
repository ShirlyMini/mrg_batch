from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

act_obj=ActionChains(driver)
logo_elem = driver.find_element(By.XPATH, "//img[@alt='geeksforgeeks-footer-logo']")
act_obj.scroll_to_element(logo_elem).perform()
# act_obj.scroll_by_amount(0,200).perform()
act_obj.scroll_by_amount(0,1000).perform()

sleep(20)