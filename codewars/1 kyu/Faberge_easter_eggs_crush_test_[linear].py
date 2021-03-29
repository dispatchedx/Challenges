import time

MOD = 998244353


def height(n, m):
    """
    :param n: number of eggs
    :param m: number of tries
    :return: total number floors
    """
    floor = 1  # recurrence variable
    total_floors = 0  # sum variable
    inverse_arr = [1]  # array of inverses till n

    # calculate first floor here so that everything else is smoothed in a single for loop
    floor = (floor * (m - 0) * inverse_arr[0]) % MOD
    total_floors = total_floors + floor

    inverse_arr = [1]
    for i in range(1, n):
        # floor division doesnt allow us to use MOD so we need to do inverse multiplication instead
        inverse_index = MOD % (i+1) - 1
        inverse = MOD - MOD // (i+1) * inverse_arr[inverse_index] % MOD
        inverse_arr.append(inverse)

        # for n of eggs, we sum nth first elements of the mth row of Pascal's triangle
        floor = (floor*(m-i) * inverse) % MOD
        total_floors = total_floors + floor

    return total_floors % MOD


#### tests #####

tests = [[1, 51, 51],
         [2, 1, 1],
         [4, 17, 3213],
         [16, 19, 524096],
         [23, 19, 524287],
         [13, 550, 621773656],
         [531, 550, 424414512],
         [10 ** 4, 10 ** 5, 132362171],
         [8*10 ** 4, 10 ** 5, 805097588],
         [8*10 ** 4, 4*10 ** 4, 616494770],
         [4*10 ** 4, 8*10 ** 4, 303227698],
         ]


#### timing function ####
def timeth():
    start = time.time()
    k = 0
    for test in tests:
        k = k+1
        res = height(test[0], test[1])
        if test[2] == res:
            res = "passed"
        else:
            res = f"failed. Expected {test[2]} got {res}"
        print(f"test {k} finished: {res}")
    end = time.time()
    print(f'test time: {end-start}')
    print("BRO!?")


timeth()

