import numpy as np


def class_entropy(P,N):
    if N==0 or P==0:
        return 0
    result = (((-P)/(P+N)*np.log2(P/(P+N)))-N/(P+N)*np.log2(N/(P+N)))
    return result


def attribute_entropy(pnlist, P, N, name):
    sum_list = []
    for attr in pnlist:
        temp = []
        for pn in attr:
            temp.append(pn)
        I = class_entropy(temp[0], temp[1])  #attr = PiNi
        entropy = (sum(attr) / (P + N))*I
        sum_list.append(entropy)
    attr_entropy = sum(sum_list)
    print(f'Entropy του {name} = sum{(sum_list)}={attr_entropy}')
    gain = class_entropy(P,N) - attr_entropy
    print(f'Gain του {name} = class entropy - {name} entropy = {gain}\n')
    return gain


# [Pi,Ni] για καθε χαρακτηριστικο
age = [[0,3],
       [2,2],
       [3,0]]

# [Pi,Ni]
competition= [[1,3],
              [4,2]]

type = [[3,3],
        [2,2]]

# P και Ν κλασης
P=3
N=2
attribute_entropy(age,P,N,"Age")
attribute_entropy(competition,P,N,"Competition")
attribute_entropy(type,P,N,"Type")

"Το χαρακτηριστικο με το μεγαλυτερο gain γινεται root, το age στη περιπτωση μας, επισης εχει 3 τιμες(old,mid,new) αρα θα εχουμε 3 κλαδια"
#αν καποιο χαρακτηριστικο ειναι 2-2 βρισκουμε παλι gain για τα υποχαρακτηριστικα του
print(f'Η εντροπια της κλασης  υπολογιζεται ως εξης (((-P)/(P+N)*np.log2(P/(P+N)))-N/(P+N)*np.log2(N/(P+N))) για P={P},N={N}= " {class_entropy(P,N)}')
