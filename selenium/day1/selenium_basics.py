from selenium import webdriver


####################################Chrome
# from selenium.webdriver.chrome.service import Service
###appr1
# service_obj = Service("E:\selenium\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
###appr2
# driver=webdriver.Chrome()
####################################Firefox
from selenium.webdriver.firefox.service import Service
###appr1
service_ff = Service("E:\selenium\drivers\geckodriver.exe")
driver = webdriver.Firefox(service=service_ff)
###appr2
# driver = webdriver.Firefox()

####################################edge
# from selenium.webdriver.edge.service import Service
###appr1
# service_edge = Service(r"E:\selenium\drivers\msedgedriver.exe")
# driver = webdriver.Edge(service=service_edge)
###appr2
# driver = webdriver.Edge()

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
print(driver.title)
driver.close()