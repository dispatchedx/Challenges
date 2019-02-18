
def find_num(ar, n):
    zeroy = -1
    for y in ar:
        zeroy += 1
        for x in y:
            if x == n:
                zerox = y.index(n)
                return zerox, zeroy


def move(ar, xy):
    x = xy[0]
    y = xy[1]
    while y != 0:
        #while y!= 0:
        temp = ar[y-1][x]
        ar[y-1][x] = ar[y][x]
        ar[y][x] = temp
        y -= 1
        # needs to return ar in each step
    while x != 0:
        # while y!= 0:
        temp = ar[y][x-1]
        ar[y][x-1] = ar[y][x]
        ar[y][x] = temp
        x -= 1
        # needs to return ar in each step
    return ar

def slide_puzzle(ar):
    zero = find_num(ar, 0)
    print(zero)
    ar = move(ar, zero)
    for col in ar:
        print(col)
    #zerox=puzzle.index(0)
    #zeroy
    print(zero)
    if puzzle[1][1]!=1:
        pass
    #    zeroy
    return ar


puzzle = [
	[4,1,3],
	[2,8,0],
	[7,6,5]
]

slide_puzzle(puzzle)

'''def move(ar, xy):
    #while ar[xy[1]-2] not in ar[0]:
    x = xy[0]
    y = xy[1]
    #while y!= 0:
    temp = ar[x][y-1]
    ar[x][y-1] = ar[x][y]
    ar[x][y] = temp

    return ar'''