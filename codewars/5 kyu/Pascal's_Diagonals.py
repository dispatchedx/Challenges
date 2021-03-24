def generate_diagonal(n, l):
    """
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
