from urllib.request import urlopen
import zipfile
import re


nothing='90052'
comments =[]
zip = zipfile.ZipFile('C:/Users/DX/Desktop/channel.zip','r')
while nothing!='':
    text=(zip.read(nothing+'.txt').decode("utf-8"))
    comments.append(zip.getinfo(nothing+'.txt').comment.decode("utf-8"))
    nothing=''.join(re.findall('Next nothing is ([0-9]+)', text))
    print(text, nothing)


print(''.join(comments))
#<!-- <-- zip -->
#now there are pairs
#channel
#Collect the comments.

