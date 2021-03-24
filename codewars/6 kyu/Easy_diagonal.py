def diagonal(n, p):
    import math

    """
    :param n:  line we end at
    :param p: number of diagonal (start from 0)
    :return:
    """
    top = (n + 1)
    bot1 = (p + 1)
    bot2 = ((n + 1) - (p + 1))
    print(top)
    print(bot1)
    print(bot2)
    return math.factorial(n + 1) / (math.factorial(p + 1) * math.factorial((n + 1) - (p + 1)))

print(diagonal(20,3))
