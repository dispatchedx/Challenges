#/usr/bin/python3
import requests
import re
from bs4 import BeautifulSoup

url = 'https://moz.com/top500'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
soup = soup.findAll('a')
for link in soup:
    print(link.get('href'))