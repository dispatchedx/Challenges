from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "eager"  # faster version

driver = webdriver.Firefox(executable_path=r'C:/Users/DX/geckodriver.exe')
driver.get("https://eclass.upatras.gr/")

name_box = driver.find_element_by_name("uname")
password_box = driver.find_element_by_name("pass")

name_box.send_keys("up1058123")
with open("C:/Users/DX/lol.txt") as myFile:
    myPass = myFile.readline()
password_box.send_keys(myPass)

login_button = driver.find_element_by_name("submit")
login_button.click()
