import urllib3
import requests
from PIL import Image
import pytesseract


headers = {
    "Host": "www.hackthis.co.uk",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.hackthis.co.uk/levels/sqli/2",
    "Cookie": "autologin=%F2%DB%B7%08%87%DE%28%C4%EA%BF6%12%D8%E6%D9%10%26%90%BA%11R%F8%04%CE%DE%28%F2%27%FE%5DH%D8%85%DBh%BF%DF%7D%91%3BG%D9%B4%A4%07%3DB%89%E4q%DD%9Dy3%A2%A94%3F%87%C4%BDS0%FF; member=1; PHPSESSID=c729sj20uj9u86n6ibkhctl1i3",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",}

#solver = CaptchaSolver('browser')
#imgurl = requests.get('https://www.hackthis.co.uk/levels/extras/captcha1.php',headers=headers)
#text = pytesseract.image_to_string(Image.open(BytesIO(imgurl.content)))
text = pytesseract.image_to_string(Image.open('TEST.png'))
textrev = text[::-1]
print(text)
print('ok')
#print(solver.solve_captcha(raw_data))


#answer=?

#get_req = requests.get("https://www.hackthis.co.uk/levels/captcha/1", headers=headers)

#post_req = requests.post("https://www.hackthis.co.uk/levels/captcha/1", data={'answer': textrev}, headers=headers)
#print(f'Original:{words}\nDecrypted:{decrypted_words}')

