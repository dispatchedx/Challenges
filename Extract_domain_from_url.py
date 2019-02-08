import re
given = "http://github.com/carbonfive/raygun"
given = 'https://www.cnet.com'
given = "http://www.zombie-bites.com"
given = "www.xakep.ru"


print(''.join(re.split('www\.|https*://|\..*', given)))


''' def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]'''

