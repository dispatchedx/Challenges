#from PIL import Image
import numpy as np
import requests
import urllib3.request
import pandas
import numpy as np

frames = pandas.DataFrame({'a':[],'b':[],'c':[]})
import tabula

dfList = tabula.read_pdf('C:/users/DX/Desktop/021.pdf', multiple_tables=True, pages='all')
#print(dfList)

frames=pandas.concat(dfList, axis=1)

print(frames)
#pandas.
    #print(df['Βαθμός'])

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