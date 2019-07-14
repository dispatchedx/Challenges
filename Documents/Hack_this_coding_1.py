
#get Words text area
#sort alphabetically
#place in correct form
#place in correct place
#submit
import urllib3
import requests
import re

payload = dict(key1='user',key2='pass')

session="xxxxxxxxxxxxxxxxxxxxxx"
headers = {"Cookie": "PHPSESSID={session}"}


get_req = requests.get("https://www.hackthis.co.uk/levels/coding/1", headers=headers)
print(get_req.status_code)
words= re.findall('<textarea>(.+)</textarea>',get_req.text)
sorted_words=', '.join(sorted(re.split(', ',words[0])))

post_req = requests.post("https://www.hackthis.co.uk/levels/coding/1", data={'answer': sorted_words}, headers=headers)
print(post_req.text)
print(f'Original:{words}\nSorted:{sorted_words}')