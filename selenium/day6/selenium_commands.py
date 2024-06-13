from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)