from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import re

"""
Plays a song from YouTube! You might get an ad though which kind of ruins this program :(
"""
#start in headless mode (invisible browser)
opts = Options()
opts.set_headless(True)
assert opts.headless

#get driver
driver = webdriver.Firefox(options=opts, executable_path=r'C:/Users/DX/geckodriver.exe')
wait = WebDriverWait(driver, 10)

#open youtube
driver.get('https://youtube.com/')
search_box = driver.find_element_by_xpath("//input[@id='search']")
search_box.click()
song = input('What song do you wanna listen to?')

#search for song
search_box.send_keys(song)
search_box.submit()

#wait 2 seconds for page to load
sleep(2)

#click on first result
results = driver.find_elements_by_xpath("//div[@id='dismissable']")
results[0].click()

#wait 2 seconds for page to load
sleep(2)

#get song name, length and current time elements
song_name = driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']").text
song_length = driver.find_element_by_xpath("//span[@class='ytp-time-duration']").text
song_current_time = driver.find_element_by_xpath("//span[@class='ytp-time-current']")
print(f'Now playing: {song_name} {song_length}')

# put a timer to check if more than 15 seconds passed after song length
time_passed = 0
string_time = song_length
string_time = re.findall('([0-9]+):([0-9]{2})', string_time)
int_song_length = int(string_time[0][0]) * 60 + int(string_time[0][1])

while 1:
    sleep(1)
    time_passed += 1

    if song_current_time.text == song_length or time_passed >= int_song_length+15:
        # close the program
        driver.close()
        quit()

