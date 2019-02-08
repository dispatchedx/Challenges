from urllib.request import urlopen
import pickle
import pprint

file = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

whats=pickle.load(file)
for line in whats:
    print(''.join([k*v for k, v in line]))
#pprint.pprint(whats)


