given = "http://github.com/carbonfive/raygun"
given = 'https://www.cnet.com'
given = "http://www.zombie-bites.com"
given = "www.xakep.ru"


def domain_name(url):
  a = 0
  b = 0
  url = url[::-1]  # i reverse the string in order to get whats between the dots aka the domain
  string = ""
  if '.' in url:
    a = url.index('.')
    url = url.replace(".", "", 1)  # remove the first dot so i can find the index of the second one if it exists

  if "." in url:
    b = url.index('.')  # if second dot exists get the second index
  else:
    b = url.index(
      ":") - 2  # if second dot doesnt exist index becomes whats 2 places after : as in https:// so we get the starting point of domain

  for l in url[a:b]:  # our string is whats between the two indexes
    string += l

  return (string[::-1])  # reverse it back to normal

''' def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]'''

