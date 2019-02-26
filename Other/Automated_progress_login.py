from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX
caps["pageLoadStrategy"] = "eager"

driver = webdriver.Firefox(desired_capabilities=caps, executable_path=r'C:/Users/DX/geckodriver.exe')
driver.get('https://progress.upatras.gr/')

name_box = driver.find_element_by_id('inputEmail')
password_box = driver.find_element_by_id('inputPassword')
with open('C:/Users/DX/lol.txt') as myFile:
    myPassword = myFile.readline()
myUsername = 'up1058123'
name_box.send_keys(myUsername)
password_box.send_keys(myPassword)

login_button = driver.find_element_by_tag_name('button')
login_button.click()
