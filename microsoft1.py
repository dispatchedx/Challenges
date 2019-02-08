import timeit
import random
def duplicates(arr):
    dups = []
    for i in range(0, len(arr)):
        if abs(arr[i]) == len(arr):
            el = -1
        else:
            el = arr[abs(arr[i])]
        if el > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        elif el == 0:
            arr[abs(arr[i])] = -len(arr)
        else:
            if abs(arr[i]) == len(arr):
                dups.append(0)
            else:
                dups.append(abs(arr[i]))
    return dups


def dupl(arr):
    dups = []
    seen = []
    for i in range(len(arr)):
        seen.append(arr[i])
        if arr[i] in seen:
            dups.append(arr[i])
    return dups



def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


arr = [0, 2, 0, 1, 3, 3]
for i in range(10000):
    arr.append(random.randint(0, 20))

wrapped = wrapper(dupl, arr)
print(timeit.Timer(wrapped).timeit(number=1000))
print(dupl(arr))
wrapped = wrapper(duplicates, arr)
print(timeit.Timer(wrapped).timeit(number=1000))
print(duplicates(arr))

