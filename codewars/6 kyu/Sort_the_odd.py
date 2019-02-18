def sort_array(source_array):
    if not source_array:
        return source_array
    else:
        odds_arr = []
        for n in source_array:
            if n % 2 == 1:
                odds_arr.append(n)
                source_array[source_array.index(n)] = -1
        odds_arr.sort()
        k = 0
        for i in source_array:
            if i == -1:
                temp = source_array.index(i)
                source_array[temp] = odds_arr[k]
                k += 1
        return source_array