from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

opts = Options()
opts.set_headless(True)
assert opts.headless

driver = webdriver.Firefox(options=opts, executable_path=r'C:/Users/DX/geckodriver.exe')

driver.get('https://bandcamp.com/')

N=7 # 8 songs per page

next_page = driver.find_elements_by_class_name('item-page')
next_page[-1].click()  # go to next page
song_list = driver.find_elements_by_css_selector('.discover-item')

song_list[N+2].click() # click on the song
print(song_list[N].text)


song_name = driver.find_element_by_class_name('title')
print(f'Song: {song_name.text} is playing now!')

seconds = 20  # seconds for song to play
for i in range(seconds):
    print(f'Time left: {seconds-i}')
    sleep(1)
driver.close()
quit()
