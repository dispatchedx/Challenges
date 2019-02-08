from urllib.request import urlopen
from PIL import Image, ImageFilter


oxygen = Image.open("C:/Users/DX/Desktop/oxygen.png")
blurred= oxygen.filter(ImageFilter.DETAIL)
#blurred.show()
print(oxygen.size)
gray=[oxygen.getpixel((x,oxygen.height/2)) for x in range(oxygen.width)]
gray=gray[::7]
gray=gray[0:-3:]
sex=[105, 110, 116, 101, 103, 114, 105, 116, 121]
text=''.join([chr(i[0]) for i in gray])
for thing in sex:
    text+=chr(thing)
print(text)
#smarty
#oxygen
#pixels???
#index??
#Created with GIMP??

