from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
preferences={"download.default_directory":r"C:\Users\user\PycharmProjects\pythonProject_March_mrng_batch\selenium\day12"}
ops_obj = webdriver.ChromeOptions()
ops_obj.add_experimental_option("prefs",preferences)
driver = webdriver.Chrome(service=service_obj, options=ops_obj)# lauching browser

driver.get("https://books-pwakit.appspot.com/")
driver.maximize_window()

shadow1=driver.find_element(By.CSS_SELECTOR, 'book-app').shadow_root
shadow1.find_element(By.CSS_SELECTOR, "input#input").send_keys("harry potter")

sleep(10)