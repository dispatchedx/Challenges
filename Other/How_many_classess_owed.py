from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



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

delay=5
myElem = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID, '0L2N11')))

time.sleep(1) #might need to increase this for slow internet speeds
#academic_progress = driver.find_element_by_id('0L2N11')
myElem.click()

#print(driver.)
#driver.close()
#idea is to use image recognition to look at vathmos field pixels if white or red?