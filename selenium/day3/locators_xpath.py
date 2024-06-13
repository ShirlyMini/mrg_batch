# xpath- absolute and relative
# abs xpath - starts from root node-/
# relative xpath - jumps to the specific node - //


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
## abs xpath
#/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input
#/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input
#/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button

# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").clear()
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").send_keys("admin@yourstore.com")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").clear()
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").send_keys("admin")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# print(driver.title)


####relative xpath
# synatx  = //tagname[@attr='value of attribute']
# driver.find_element(By.XPATH,"//input[@id='Email']").clear()
# driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
# driver.find_element(By.XPATH,"//input[@class='password']").clear()
# driver.find_element(By.XPATH,"//input[@class='password']").send_keys("admin")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# print(driver.title)

#styntac = //tagname[text()='innertext']
driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//input[@class='password']").clear()
driver.find_element(By.XPATH,"//input[@class='password']").send_keys("admin")
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
print(driver.title)
##if any spaces involved in innertext
# syntax //tagname[contains(text(), 'partial innertext')]
# syntax //tagname[contains(@attr, 'partial valueof attr')]

# //a[contains(text(),'Ambo Agritec')]
# //input[contains(@name, 'username')]

###synatx //tagname[starts-with(text(), 'partial innertext')]
###synatx //tagname[starts-with(@attr, 'partial valueof attr')]
# //input[starts-with(@name, 'email')]


####using and/or operator
# //tagname[@attr='value of attribute' and @attr1='value of attr1']
# //tagname[@attr='value of attribute' or @attr1='value of attr1']
# //tagname[@attr='value of attribute' and contains(text(), 'partial innertext')]
# //tagname[@attr='value of attribute' or contains(text(), 'partial innertext')]

# //input[@type='text' and @name='phone']# matches only one elem
# //input[@type='text' or @name='phone']# match 4 diff elem




