from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
#### tabbed window
# driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
# print(driver.window_handles)# return list of browser id[prarent browser id, child browser id]
# #['0EFEF48B65CAC674ED1F25ADD9D613EB', 'FBC2891DD0CF873CF1853A2B943DFCF2']
# parent_id=driver.window_handles[0]
# child_id=driver.window_handles[1]
# print(driver.title)
# driver.switch_to.window(child_id)
# print(driver.title)
### new window
driver.find_element(By.XPATH, "//a[text()='Open New Seperate Windows']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
print(driver.window_handles)# return list of browser id[prarent browser id, child browser id]
#['0EFEF48B65CAC674ED1F25ADD9D613EB', 'FBC2891DD0CF873CF1853A2B943DFCF2']
parent_id=driver.window_handles[0]
child_id=driver.window_handles[1]
print(driver.title)
driver.switch_to.window(child_id)
print(driver.title)

#####driver.close vs driver.quit
driver.switch_to.window(parent_id)
driver.close()
# driver.quit()
sleep(10)