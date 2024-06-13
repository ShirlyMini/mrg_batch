import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def launch_setup():
    service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    yield driver
    driver.quit()