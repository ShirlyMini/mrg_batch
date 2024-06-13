from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

###radio button
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]').click()
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)
# alt_ref.accept()

# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# sleep(2)
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)
# # alt_ref.accept()
# alt_ref.dismiss()

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
sleep(2)
alt_var = driver.switch_to.alert
print(alt_var.text)
alt_var.send_keys("welcome")
# alt_var.accept()
alt_var.dismiss()

sleep(10)