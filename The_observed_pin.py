observed = '11'
mydict = {'1': ['1', '2', '4'],
          '2': ['2', '1', '5', '3'],
          '3': ['3', '2', '6'],
          '4': ['4', '1', '7', '5'],
          '5': ['5', '2', '4', '8', '6'],
          '6': ['6', '3', '5', '9'],
          '7': ['7', '4', '8'],
          '8': ['8', '5', '7', '0', '9'],
          '9': ['9', '6', '8'],
          '0': ['0', '8']
          }
arrays = []
final = []

for l in observed:
  arrays.append(mydict[l])

'''number_of_letters = len(observed)
k= 0
for i in range(number_of_letters):
  for j in range(len(arrays[i])):
    final.append(arrays[i][k] + arrays[i][j])
  k +=1'''
if len(observed) == 1:
  for l in arrays[0]:
    final.append(l)
if len(observed) == 2:
  for l in arrays[0]:
    for k in arrays[1]:
      final.append(l+k)
if len(observed) == 3:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        final.append(l+k+j)
if len(observed) == 4:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        for a in arrays[3]:
          final.append(l+k+j+a)
if len(observed) == 5:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        for a in arrays[3]:
          for b in arrays[4]:
            final.append(l+k+j+a+b)
if len(observed) == 6:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        for a in arrays[3]:
          for b in arrays[4]:
            for c in arrays[5]:
              final.append(l+k+j+a+b+c)
if len(observed) == 7:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        for a in arrays[3]:
          for b in arrays[4]:
            for c in arrays[5]:
              for d in arrays[6]:
                final.append(l+k+j+a+b+c+d)
if len(observed) == 8:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        for a in arrays[3]:
          for b in arrays[4]:
            for c in arrays[5]:
              for d in arrays[6]:
                for e in arrays[7]:
                  final.append(l+k+j+a+b+c+d+e)


print(" ")
print(arrays)
print(final)









if len(observed) == 1:
  for l in arrays[0]:
    final.append(l)
if len(observed) == 2:
  for l in arrays[0]:
    for k in arrays[1]:
      final.append(l+k)
if len(observed) == 3:
  for l in arrays[0]:
    for k in arrays[1]:
      for j in arrays[2]:
        final.append(l+k+j)
