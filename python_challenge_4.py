import urllib.request
import re
i = 0
req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022')
while i < 400:
    string = urllib.request.urlopen(req)
    string = str(string.read())
    print(string)
    nothing=''.join(re.findall('next nothing is ([0-9]+)', string))
    print(nothing)
    req='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing
    i += 1


  #and the next nothing is 44827
  #linkedlist
  #chain
  #urllib
  #dont try all nothtings 400 enough