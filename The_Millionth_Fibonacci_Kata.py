import time
N = 1000000
print(f'Calculating {N}th fibonacci number..')
def fib(n):
    """ Calculates Nth fibonacci number in Θ(log n) complexity (works with negative values)"""
    if n == 0:
        return 0
    elif n <= 2 and n>0:
        return 1
    elif n==-1:
        return 1

    else:
        k = n >> 1                   # if n is odd; k=(n/2) ### if n is even; k=(n-1)/2
        a = fib(k)                   # F(k)
        b = fib(k+1)                 # F(k+1)
        if n & 1:                    # if odd;
            d = a * a + b * b        # F(k)^2 + F(k+1)^2
            return d
        else:                        # if even;
            c = a * ((b << 1) - a)   # F(k)*[2F(k+1)-F(k)]
            return c


start = time.time()
x = fib(N)
end = time.time()
print(f'{x}, finished in {end-start} seconds')
