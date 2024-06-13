import pytest
from selenium.webdriver.common.by import By

class Test_NoP_Commerce_login:
    def test_case_verify_login_page_title(self, launch_setup):
        driver=launch_setup
        print(driver.title)
        if driver.title=="Your store. Login":
            assert True
        else:
            assert False

    def test_case_verify_dashbord_page_title(self, launch_setup):
        driver=launch_setup
        driver.find_element(By.XPATH,"//input[@id='Email']").clear()
        driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("admin@yourstore.com")
        driver.find_element(By.XPATH,"//input[@class='password']").clear()
        driver.find_element(By.XPATH,"//input[@class='password']").send_keys("admin")
        driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        print(driver.title)
        if driver.title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

    @pytest.mark.parametrize("user, pswd, expected", [("admin@yourstore.com", "admin", "True"), ("admin","admin", "False"),("admin@yourstore.com", "admin123", "False"), ("admin", "admin123", "False")])
    def test_case_verify_login_ddt(self,launch_setup, user, pswd, expected):
        driver = launch_setup
        driver.find_element(By.XPATH,"//input[@id='Email']").clear()
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(user)
        driver.find_element(By.XPATH,"//input[@class='password']").clear()
        driver.find_element(By.XPATH,"//input[@class='password']").send_keys(pswd)
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        if driver.title == "Dashboard / nopCommerce administration" and expected=="True":
            assert True
        elif driver.title != "Dashboard / nopCommerce administration" and expected=="False":
            assert True
        else:
            assert False
