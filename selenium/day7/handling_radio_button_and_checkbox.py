from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

###radio button
driver.get("https://www.facebook.com/signup")
driver.maximize_window()

driver.find_element(By.XPATH, "//label[text()='Male']/following-sibling::input").click()

sleep(10)