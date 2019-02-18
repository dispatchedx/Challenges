from urllib.request import urlopen
from PIL import Image, ImageFilter
import time

test_array = []
for i in range(1, 20000000):
    test_array.append(i)
#test_array = set(test_array) - {100000}
def missing_number(given_array):
    should_be = 0
    for num in given_array:
        should_be += 1
        if num!= should_be:
            missingNumber = num-1
            should_be += 1
            break
    return missingNumber


def missing_number_sum(given_array):
    #sum = n * (n - 1)//2
    array_length = len(given_array)
    total = (array_length + 1) * (array_length + 2) // 2
    for c in given_array:
        total -= c
    missingNumber = total
    return missingNumber

k=7
start = time.time()
result = missing_number(test_array)
end = time.time()
print(f'{result} in {end-start}')
start = time.time()
result = missing_number_sum(test_array)
end = time.time()
print(f'{result} in {end-start}')
#if result==arr:
#    print('No changes')













'''def miNN(arr, N):
    index = []
    for i in range(0, N):
        min = arr[0]
        for num1 in arr:
            if num1 < min:
                min = num1
        if i != N:
            arr.remove(min)
    return min'''





















#working hard?
#integrity width=640 height=480 border=0
#notinsect
#poly
#Where is the missing link color="#303030" size="+2"
#oxygen
#<!-- INFLATE #########
#coords="179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282"

#un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
#
