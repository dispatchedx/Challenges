def lel():
  secret = "whatisup"
  triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
  ]
  array = []
  tmpArr = triplets[3]
  def sorting(tmpArr, array):
      if tmpArr[0] not in array and tmpArr[1] not in array and tmpArr[2] not in array:
          array.append(tmpArr[0])
          array.append(tmpArr[1])
          array.append(tmpArr[2])
      elif tmpArr[0] in array and tmpArr[1] in array and tmpArr[2] not in array:
          array.insert(array.index(tmpArr[1])+1,tmpArr[2]) # prepei na mpei meta to 2o kapos
      elif tmpArr[0] in array and tmpArr[1] not in array and tmpArr[2] in array:
          array.insert(array.index(tmpArr[0])+1,tmpArr[1]) # care
      elif tmpArr[0] not in array and tmpArr[1] not in array and tmpArr[2] in array: # this one isnt used
          array.insert(array.index(tmpArr[2]), tmpArr[1])
          array.insert(array.index(tmpArr[1]), tmpArr[0])
      elif tmpArr[0] not in array and tmpArr[1] in array and tmpArr[2] not in array:
          array.insert(array.index(tmpArr[1])+1,tmpArr[2]) # how does -1 in this make a second b appear????
          array.insert(array.index(tmpArr[1]),tmpArr[0]) #www
      elif tmpArr[0] not in array and tmpArr[1] in array and tmpArr[2] in array:
          array.insert(array.index(tmpArr[1]),tmpArr[0])
      elif tmpArr[0] in array and tmpArr[1] not in array and tmpArr[2] not in array:
          array.insert(array.index(tmpArr[0]) + 1, tmpArr[2])
          array.insert(array.index(tmpArr[0]) + 1, tmpArr[1])
      elif tmpArr[0] in array and tmpArr[1] in array and tmpArr[2] in array:
          if array.index(tmpArr[0]) > array.index(tmpArr[1]): #magic happens here
              array.remove(tmpArr[0])
              array.insert(array.index(tmpArr[1]), tmpArr[0])
          if array.index(tmpArr[0]) > array.index(tmpArr[2]):
              array.remove(tmpArr[0])
              array.insert(array.index(tmpArr[2]),tmpArr[0])
          if array.index(tmpArr[1]) > array.index(tmpArr[2]):
              array.remove(tmpArr[1])
              array.insert(array.index(tmpArr[2]), tmpArr[1])

  for i in range(2): # putting it in a loop for once fixes everything
    for i in range(len(triplets)):
        tmpArr = triplets[i]
        sorting(tmpArr, array)
  '''for i in range(2):
      tmpArr = ['a','b','c']
      sorting(tmpArr,array)
      tmpArr = ['c','i','t']
      sorting(tmpArr, array)
      tmpArr = ['g','h','i']
      sorting(tmpArr, array)
      tmpArr = ['d', 'o', 's']
      sorting(tmpArr, array)
      tmpArr = ['e', 'f', 'z']
      sorting(tmpArr, array)
      tmpArr = ['r', 's', 't']
      sorting(tmpArr, array)
      tmpArr = ['e', 'g', 'i']
      sorting(tmpArr, array)
      tmpArr = ['h', 'j', 'k']
      sorting(tmpArr, array)
      tmpArr = ['c', 'e', 'w']
      sorting(tmpArr, array)'''

  print(''.join(array))

lel()