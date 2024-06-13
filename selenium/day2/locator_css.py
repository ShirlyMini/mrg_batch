#syntax
# tagname#valueofid(tagname id optional)
# #valueofid

#tagname.valueofclass(tagname id optional)
#.valueofclass

# tagname#id.class[attr=valueofattr]

#tagname[attr=valueofattr](tagname id optional)
#[attr=valueofattr]

### example 1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
# example with id
driver.find_element(By.CSS_SELECTOR, "input#Email").clear()
# example with id and class
driver.find_element(By.CSS_SELECTOR, "input#Email.email").send_keys("admin@yourstore.com")
# example with id and class
driver.find_element(By.CSS_SELECTOR, "input#Password.password").clear()
# example without using tagname
driver.find_element(By.CSS_SELECTOR, "#Password.password").send_keys("admin")

driver.find_element(By.CSS_SELECTOR,'[type=submit]').click()

print(driver.title)