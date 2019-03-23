from PIL import Image
import numpy as np
import requests
import io
response = requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg', auth=('huge', 'file'))

im = Image.open(io.BytesIO(response.content))
image_array = np.asarray(im)
odd = []
even = []
width = im.width
height = im.height
for x in range(height):
    if x % 2 == 0:
        odd.append(image_array[x][::2])
    else:
        even.append(image_array[x][::2])
odd = np.asarray(odd)
even = np.asarray(even)
#print(image_array[0][::2])
Image.fromarray(odd).show()
Image.fromarray(even).show()
#print(im)


