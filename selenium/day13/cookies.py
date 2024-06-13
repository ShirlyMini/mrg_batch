from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service("E:\selenium\drivers\chromedriver.exe")
preferences={"download.default_directory":r"C:\Users\user\PycharmProjects\pythonProject_March_mrng_batch\selenium\day12"}
ops_obj = webdriver.ChromeOptions()
ops_obj.add_experimental_option("prefs",preferences)
driver = webdriver.Chrome(service=service_obj, options=ops_obj)# lauching browser

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()

# all_cookies=driver.get_cookies()
# print(all_cookies)

# [{'domain': 'admin-demo.nopcommerce.com', 'httpOnly': True, 'name': '.Nop.Antiforgery', 'path': '/', 'sameSite': 'Strict', 'secure': True, 'value': 'CfDJ8PWCLA4dRNhKnbe8oYbH17Cp-dXcWEct9l2beRgdY-jZIg7gzP_UXjo0EttYPwrd2Dw5pgbiPChvsRqNRHngcTWjLfyu8sHaxp9VY6NOKSDnA2o30FuZJOhy1ZPxk4dVrxpQonAWQsVPqZ04sj-fuko'},
# {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1747794789, 'httpOnly': False, 'name': '.Nop.Culture', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'c%3Den-US%7Cuic%3Den-US'},
# {'domain': 'admin-demo.nopcommerce.com', 'expiry': 1747794789, 'httpOnly': True, 'name': '.Nop.Customer', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '408552dd-d7e9-4c63-8444-03ebc5887b62'}]


#add cookies
driver.add_cookie({'name':"mycookie", "value":"123456789"})
print(driver.get_cookie('mycookie'))
#{'domain': 'admin-demo.nopcommerce.com', 'httpOnly': False, 'name': 'mycookie', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '123456789'}

# delete cookie
driver.delete_cookie('mycookie')
for cookie in driver.get_cookies():
    print(cookie)


print(driver.get_cookie('mycookie'))#None
