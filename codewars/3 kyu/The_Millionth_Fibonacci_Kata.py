def fib(n):
    """ Calculates Nth fibonacci number in Θ(log n) complexity using the fast doubling method.
    It works with negative values as well """
    if n == 0:
        return 0

    elif 2 >= n > 0:
        return 1
    elif n == -1:
        return 1

    else:
        k = n >> 1
        a = fib(k)                   # F(k)
        b = fib(k+1)                 # F(k+1)
        if n & 1:                    # if odd;
            d = a * a + b * b        # F(k)^2 + F(k+1)^2
            return d
        else:                        # if even;
            c = a * ((b << 1) - a)   # F(k)*[2F(k+1)-F(k)]
            return c
