def flip(arr,k):
    """ Flips k first elements in an array """
    if k>len(arr):
        exit("Array not big enough")
    for i in range(k//2):
        temp = arr[k-i-1]
        arr[k-i-1] = arr[i]
        arr[i] = temp
    return arr


def pancakeSort(arr):
    """ Uses flip function to sort an array """
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr = flip(arr, i+1)
                arr = flip(arr, i+2)
                arr = flip(arr, i+1)
                is_sorted = False
                break
    return arr