from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

'''It doesn't really send a message yet'''


driver = webdriver.Firefox(executable_path='C:/Users/DX/geckodriver.exe')

driver.get('https://www.facebook.com/messages')


name_box = driver.find_element_by_id('email')
pass_box =driver.find_element_by_id('pass')

name_box.send_keys('my_email')  # replace my_email with your email
pass_box.send_keys('my_pass')   # replace my_pass with your password
pass_box.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
message_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3ixn')))
message_box.click()
driver.execute_script("""
var element = document.querySelector("._3ixn");
if (element)
    element.parentNode.removeChild(element);
""")

message_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div textarea.uiTextareaNoResize')))
message_box.click()
message_box.send_keys('test')

