# implicit and explicit wait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.implicitly_wait(10)
wait_obj = WebDriverWait(driver,10)

print(driver.find_element(By.ID, 'RememberMe').is_displayed())
wait_obj.until(expected_conditions.presence_of_element_located((By.ID, "RememberMe")))
print(driver.find_element(By.ID, 'RememberMe').is_selected())
driver.find_element(By.ID, 'RememberMe').click()
print("After clicking checkbox....")
print(driver.find_element(By.ID, 'RememberMe').is_selected())

