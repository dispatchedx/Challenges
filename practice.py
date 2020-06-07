from PIL import Image
import numpy as np
import requests
import urllib3.request


url = 'https://progress.upatras.gr/'
response = requests.get(url)
print(response.content)
'''
response = requests.get('http://www.pythonchallenge.com/pc/return/evil1.jpg', auth=('huge', 'file'))
response = (response.content)
print(response)
#im = Image.open(io.BytesIO(response.content))
im1 = Image.open('c:/users/dx/desktop/evil1.jpg')
im2 = Image.open('c:/users/dx/desktop/evil2.jpg')
im3 = Image.open('c:/users/dx/desktop/evil3.jpg')
image_array = np.asarray(im1)

#im2.show()
#im3.show()
im1.close()
im2.close()
im3.close()
#print(im)

############## Bert is evil! go back! #############
'''