#/usr/bin/python3
import requests
import re

url = 'https://moz.com/top500'
response = requests.get(url)
links = '\n'.join(re.findall("(?:href=)\"(https?://[^\"]+)",response.text))
print(links)


