message = input()
binary = ''
temp_list = []
for c in message:
    temp_list.append(ord(c))                # put the message in a list
for c in temp_list:                         # For each letter, translate it to binary and put it in a string
    c = bin(c)
    c = c[2:]
    c = c.zfill(7)
    binary = binary + c

index = 0
print(binary)
listed = []

while index <= len(binary) - 1:
    digit = binary[index]
    if digit == '1':
        listed.append(' 0 ')
        index += 1
        dex = index
        for digit in binary[dex-1:]:
            if digit == '1':
                dex += 1
                listed.append('0')
            else:
                index = dex-1
                break
        else:
            index = dex

    if digit == '0':
        listed.append(' 00 ')
        index += 1
        dex = index
        for digit in binary[dex-1:]:
            if digit == '0':
                dex += 1
                listed.append('0')
            else:
                index = dex-1
                break
        else:
            index = dex

listed = ''.join(listed)
print(listed[1:])
''' message = input()
encoded = ''
for c in message:
    encoded = encoded + str(ord(c))
encoded = int(encoded)

binary = bin(encoded)
binary = binary[2:]
binary = binary.zfill(7)
# print(binary)
index = 0
#print(binary)
listed = []
#binary = '10000111000011'
while index <= len(binary) - 1:
    digit = binary[index]
    if digit == '1':
        listed.append(' 0 ')
        index += 1
        dex = index
        for digit in binary[dex-1:]:
            if digit == '1':
                dex += 1
                listed.append('0')
            else:
                index = dex-1
                break
        else:
            index = dex

    if digit == '0':
        listed.append(' 00 ')
        index += 1
        dex = index
        for digit in binary[dex-1:]:
            if digit == '0':
                dex += 1
                listed.append('0')
            else:
                index = dex-1
                break
        else:
            index = dex

listed = ''.join(listed)
print(listed[1:])
    '''