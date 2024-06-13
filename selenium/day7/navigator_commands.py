from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.get("https://www.linkedin.com/learning-login")
driver.back()
assert driver.title=="Your store. Login"# nop commerce
driver.refresh()
assert driver.title=="Your store. Login"# nop commerce
driver.forward()
assert driver.title=="LinkedIn Learning | Login"
driver.refresh()
