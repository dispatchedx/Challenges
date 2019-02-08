def disemvowel(string):

    return ''.join(c for c in string if c.lower() not in 'aeiou')


print(disemvowel("This website is for losers LOL!"))

