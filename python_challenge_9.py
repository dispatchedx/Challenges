from urllib.request import urlopen
from PIL import ImageDraw, Image
import re
im = Image.open('C:/Users/DX/Desktop/good.jpg')

with open('coords1.txt') as coordsFile:
    coords = coordsFile.readlines()
coords = ''.join(coords)
listing = list(re.findall('\d+',coords))
inting = []
for x in listing:
    inting.append(int(x))
tupling = tuple(inting)
print(f'{tupling}\n')
draw = ImageDraw.Draw(im)
draw.polygon(tupling, fill=128)
im.show()


