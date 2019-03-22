def look_and_say(n):
    n = list(str(n))
    result = []
    temp = -1
    i = 0
    while True:
        count = 0
        for k in range(len(n)):
            if n[k] == n[0]:
                count += 1
                temp = n[i]
            else:
                result.append(str(count))
                result.append(temp)
                for x in range(count):
                    del n[0]
                    k = k-1
                i = i-1
                break
        else:
            result.append(str(count))
            result.append(temp)
            break
        i += 1
    return result


n = 1
for i in range(1, 31):
    n = ''.join(look_and_say(n))
    print(f'len(a[{i}]) = {len(n)}')
