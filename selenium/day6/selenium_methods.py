# findelements and findelement

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()

### find element
# locator matching single elem
#//table[@class='dataTable']/tbody/tr[1]/td/a
# print(driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td/a").text)
# # locator matching multiple elem
# print(driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr/td/a").text)
# # invalid
# print(driver.find_element(By.XPATH, "//table[@class='dataTable']/tbodylkldockw/td/a").text)#selenium.common.exceptions.NoSuchElementException


### find elements
# locator matching single elem
# list_of_webelem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td/a")
# print(list_of_webelem)
# for elem in list_of_webelem:
#     print(elem.text)

# locator matching multiple elem
# list_of_webelem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbody/tr/td/a")
# for elem in list_of_webelem:
#     print(elem.text)

# invalid
list_of_webelem = driver.find_elements(By.XPATH, "//table[@class='dataTable']/tbodygfsgsag/td/a")
print(list_of_webelem)
for elem in list_of_webelem:
    print(elem.text)