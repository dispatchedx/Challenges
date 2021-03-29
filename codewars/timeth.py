import time
def timeth(func,tests):
    start = time.time()
    k = 0
    for test in tests:
        k = k+1
        res = func(test[0], test[1])
        if test[-1] == res:
            res = "passed"
        else:
            res = f"failed. Expected {test[2]} got {res}"
        print(f"test {k} finished: {res}")
    end = time.time()
    print(f'test time: {end-start}')
    print("BRO!?")
