def last_digit(lst):
    """ Returns the last digit of a power tower x^y^z^..."""

    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0] % 10

    def _last_digit(n1, n2):
        x = pow(n1, n2, 1000)
        if n1 * n2 != 0 and x == 0:  # if n1*n2!=0 and x==0 then we dont deal with a 0 but with numbers ending with 0s so return 100 (its the same)
            return 100
        else:
            return x  # last digit of n1**n2

    lst = lst[::-1]
    while len(lst) > 1:
        lst[1] = _last_digit(lst[1], lst[0])
        del lst[0]
    return lst[0] % 10

'''usage: print(last_digit([2, 2, 101, 2]))'''
