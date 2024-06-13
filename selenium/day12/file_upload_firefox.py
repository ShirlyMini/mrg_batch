from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\geckodriver.exe")
#setting
ops_obj=webdriver.FirefoxOptions()
ops_obj.set_preference("browser.download.folderList",2)#0-desktop,1-downloadfolder,2-desiredloc
ops_obj.set_preference("browser.download.dir",r"C:\Users\user\PycharmProjects\pythonProject_March_mrng_batch\selenium\day12")#onlythefolderlistis2
# ops_obj.add_argument("--headless")
ops_obj.add_argument("--start-maximized")
driver = webdriver.Firefox(service=service_obj, options=ops_obj)# lauching browser

driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
### drpdown without select/option
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]/ancestor::a/following-sibling::ul/li/a/p[contains(text(),'Customers')]").click()
sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success dropdown-toggle']").click()
driver.find_element(By.NAME, "exportexcel-all").click()
sleep(7)