import urllib3
import requests
import re


session="xxxxxxxxxxxxxxxxxxxxxx"
headers = {"Cookie": "PHPSESSID={session}"}



def decrypt(encrypted_words): #-> Char list
    decrypted_words=[]
    total_visible_ASCII=126
    for num in encrypted_words:
        if num is not ' ':
            new_value = (total_visible_ASCII-int(num))
            current = new_value+32
            decrypted_words.append(chr(current))
        else:
             decrypted_words.append(' ')
    return decrypted_words

get_req = requests.get("https://www.hackthis.co.uk/levels/coding/2", headers=headers)
words= re.findall('<textarea>(.+)</textarea>',get_req.text)
words=(re.split(',',words[0]))
decrypted_words=''.join(decrypt(words))
post_req = requests.post("https://www.hackthis.co.uk/levels/coding/2", data={'answer': decrypted_words}, headers=headers)
print(f'Original:{words}\nDecrypted:{decrypted_words}')