from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

right_click = driver.find_element(By.XPATH, "//span[text()='right click me']")
dble_clk = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")

# act_obj = ActionChains(driver)
# act_obj.context_click(right_click).perform()
# driver.find_element(By.XPATH, "//span[text() = 'Copy']").click()
# alt_ref = driver.switch_to.alert
# print(alt_ref.text)
# alt_ref.accept()

act_obj=ActionChains(driver)
act_obj.double_click(dble_clk).perform()
alt_ref= driver.switch_to.alert
print(alt_ref.text)
alt_ref.accept()

sleep(10)