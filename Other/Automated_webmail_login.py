from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:/users/DX/geckodriver.exe')

driver.get('https://webmail.ceid.upatras.gr/')

username_box = driver.find_element_by_id('rcmloginuser')
username_box.send_keys('stsimpoukis')

password_box = driver.find_element_by_id('rcmloginpwd')
with open('C:/users/DX/web.txt') as passwordFile:
    myPassword = passwordFile.readline()
password_box.send_keys(myPassword)

login_button = driver.find_element_by_id('rcmloginsubmit')
login_button.click()
