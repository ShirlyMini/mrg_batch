from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

l_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
r_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

act_obj=ActionChains(driver)
# print(l_slider.location)#{'x': 59, 'y': 250}
# act_obj.drag_and_drop_by_offset(l_slider,100, 0).perform()
# print(l_slider.location)

print(r_slider.location)#{'x': 545, 'y': 250}
act_obj.drag_and_drop_by_offset(r_slider, -100,0).perform()
print(r_slider.location)
act_obj.drag_and_drop_by_offset(r_slider, 100,0).perform()
print(r_slider.location)