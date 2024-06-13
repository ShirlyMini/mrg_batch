from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@type='submit']").click()
### drpdown without select/option
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]/ancestor::a/following-sibling::ul/li/a/p[contains(text(),'Products')]").click()
sleep(7)
### with select/option
drp_down_elem =driver.find_element(By.NAME, "products-grid_length")
drp_down_obj = Select(drp_down_elem)
# drp_down_obj.select_by_visible_text("100")
# drp_down_obj.select_by_value("50")
drp_down_obj.select_by_index(0)# 0 to n-1

sleep(20)