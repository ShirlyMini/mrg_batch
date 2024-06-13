from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
elem = driver.find_element(By.ID, "singleframe")
driver.switch_to.frame(elem)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()
##frame1
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='Multiple']/iframe"))
# Frame2
driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='iframe-container']/iframe"))
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")
## move from frame2 to frameone
driver.switch_to.parent_frame()
print(driver.find_element(By.XPATH,"//div[@class='iframe-container']/h5").text)

sleep(10)