from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

###radio button
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]/ancestor::a/following-sibling::ul/li/a/p[contains(text(),'Products')]").click()
sleep(7)
list_of_elem = driver.find_elements(By.XPATH, "//table[@id='products-grid']/tbody/tr/td[1]/input")
for elem in list_of_elem:
    elem.click()

sleep(60)
