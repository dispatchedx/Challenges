import pytesseract
import requests
from PIL import Image
from subprocess import check_output
import re
from io import BytesIO
import time

def resolve(path):
    """
        Resamples the image and returns the guessed string
    """
    print("Resampling the Image")
    check_output(['convert', path, '-resample', '300', path])
    return pytesseract.image_to_string(Image.open(path),config='--psm 7')

#TODO censor cookie
headers = {"Cookie": "PHPSESSID=c729sj20uj9u86n6ibkhctl1i3",}


def attempt():
    image_url = requests.get('https://www.hackthis.co.uk/levels/extras/captcha2.php',headers=headers)
    im = Image.open(BytesIO(image_url.content))
    local_image = im.save('tmp.png')
    print('Resolving Captcha')
    captcha_text = resolve('tmp.png')
    #tesserac mistakenly adds spaces, there will never be any spaces given
    ##captcha_text= captcha_text.replace(" ", "")
    #challenge asks for reversed
    #post_req = requests.post("https://www.hackthis.co.uk/levels/captcha/2", data={'answer': captcha_text}, headers=headers)
    print('Extracted Text',captcha_text)
    im.show()

# Alot of atempts, there are larger or small mistakes, one will eventually be correct
attempt()
'''for i in range(100):
    attempt()
    time.sleep(5)'''