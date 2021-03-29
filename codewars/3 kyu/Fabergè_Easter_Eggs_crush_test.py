def height(n, m):
    """
    :param n: number of eggs
    :param m: number of tries
    :return: total number floors
    """
    floor = 1
    total_floors = 0
    # Calculates mth row of Pascal's triangle
    for i in range(n):
        floor = (floor*(m-i)//(i+1))
        total_floors = total_floors + floor
    # Depending on n of eggs, we sum nth first elements of the row
    return total_floors
