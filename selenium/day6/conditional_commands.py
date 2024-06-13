# is_displayed()
# is_selected()--checkbox, radio button
# is_enabled()--


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

####is_displayed and is_selected
# driver.get("https://admin-demo.nopcommerce.com/")
#
# print(driver.find_element(By.ID, 'RememberMe').is_displayed())
# print(driver.find_element(By.ID, 'RememberMe').is_selected())
# driver.find_element(By.ID, 'RememberMe').click()
# print("After clicking checkbox....")
# print(driver.find_element(By.ID, 'RememberMe').is_selected())

#####is_enabled
driver.get("https://www.linkedin.com/learning-login/")
print(driver.find_element(By.ID, 'auth-id-button').is_enabled())# False
driver.find_element(By.ID, 'auth-id-input').send_keys("abc@gmail.com")
print(driver.find_element(By.ID, 'auth-id-button').is_enabled())# True

