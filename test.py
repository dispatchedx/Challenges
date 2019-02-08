import math
def encryption(s):
    temp = []
    result =''
    rows = int(math.sqrt(len(s)))
    col = rows+1
    x= 0
    for i in range(rows):
        temp.append(s[x:col+x])
        x+=col
    for c in range(col):

        for r in range(rows):
            if r >= len(temp[c]):
                break
            result+= temp[r][c]
        result+= ' '




    print(result)
encryption('feedthedog')



