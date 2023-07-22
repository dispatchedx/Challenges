import re
"""
from: 
https://ffxiv.gamerescape.com/wiki/Spodumene

"""
with open("C:/Users/DX/Desktop/materials.txt") as f:
    lines = f.readlines()
    my_dict = {}
    for i in range(len(lines)):
        lines[i] = re.sub('\\n|\\t|75', '', lines[i])
        lines[i] = re.findall('([0-9].*?) Icon',  lines[i])

    processed_lines = [x for x in lines if x]

    for i in range(len(processed_lines)):
        key = processed_lines[i][0:][0][1:]
        value = int(processed_lines[i][0:][0][0])
        if key not in my_dict:
            my_dict[key] = value
        else:
            my_dict[key] = my_dict[key]+value


#print(my_dict)
for key, value in my_dict.items():
    print(key, value)


#for i in range(97,119):
 #   print(f'=COUNTIF({chr(i).upper()}2:{chr(i).upper()}10,"*")')


