def generate_diagonal(n, l):
    """
    really slow cause it sums array in a nested for
    better to just generate the last array by definition like:
    return [factorial(n+i) // (factorial(n) * factorial(i)) for i in range(l)]
    :param l:  line we end at (start from 0)
    :param n: number of diagonal (start from 0)
    :return:
    """
    res = []
    arr = [1] * l
    l = l+1
    for diag in range(n):
        res = []
        for index in range(1, l):
            summed = sum(arr[:index])  # sum is really slow for large numbers
            res.append(summed)
        arr = res
    return (arr)
