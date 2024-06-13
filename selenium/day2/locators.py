# address of element


# normal locator- id(unique and fastest), name(unique), class, tagname, linktext/partiallinktext
# custom locator - css, xpath(write on our own)

# <input
# class="email input-validation-error"
# value="admin@yourstore.com"
# autofocus="autofocus"
# type="email"
# data-val="true"
# data-val-regex="Wrong email" data-val-regex-pattern="^(([^<>()\[\]\\.,;:\s@&quot;]+(\.[^<>()\[\]\\.,;:\s@&quot;]+)*)|(&quot;.+&quot;))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
# data-val-required="Please enter your email"
# id="Email"
# name="Email"
# aria-describedby="Email-error"
# aria-invalid="true" data-gtm-form-interact-field-id="0">ksamdxjd<


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
# driver.maximize_window()
# ##### Example 1(ID)
# driver.find_element(By.ID, "Email").clear()
# driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID, "Password").clear()
# driver.find_element(By.ID, "Password").send_keys("admin")
# ####example for tagname
# driver.find_element(By.TAG_NAME, "button").click()
#
# print(driver.title)
# driver.close()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service_obj = Service("E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
##### Example 3(name)
driver.find_element(By.NAME, 'Email').clear()
driver.find_element(By.NAME, 'Email').send_keys("admin@yourstore.com")
driver.find_element(By.NAME, 'Password').clear()
driver.find_element(By.NAME, 'Password').send_keys("admin")
###Example 4(classname)
# driver.find_element(By.CLASS_NAME,'button-1 login-button').click()# wont work
driver.find_element(By.CLASS_NAME,'login-button').click()
print(driver.title)
sleep(7)
###Exapmle 5(linktext/partial linktext) -tag a
driver.find_element(By.LINK_TEXT, "Logout").click()

print(driver.title)
driver.close()