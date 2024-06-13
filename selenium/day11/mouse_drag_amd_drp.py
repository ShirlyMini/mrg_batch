from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
driver.maximize_window()

s1=driver.find_element(By.ID, "box2")
s2=driver.find_element(By.ID, "box3")
d1=driver.find_element(By.ID, "box102")
d2=driver.find_element(By.ID, "box103")

act_obj = ActionChains(driver)
act_obj.drag_and_drop(s1,d1).perform()
act_obj.drag_and_drop(s2,d2).perform()

sleep(10)