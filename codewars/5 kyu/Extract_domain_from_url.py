''' Extracts the  domain from a given url '''

import re
given = {"http://github.com/carbonfive/raygun",'https://www.cnet.com',"http://www.zombie-bites.com","www.xakep.ru"}

for url in given:
    print(''.join(re.split('www\.|https*://|\..*', url)))

