while 1:
    number = int(input())
    roman = ''


    def encoder(num, let, nlet, nnlet, roman=''):  # final
        if num == 9:
            roman += let + nnlet
        if 4 < num < 9:
            roman += nlet
            for i in range(num-5):
                roman += let
        if num == 4:
            roman += let + nlet
        if num <= 3:
            for i in range(num):
                roman += let
        return roman

    while True:
        if number >= 1000:
            roman += 'M'
            number -= 1000
        if number <= 999:
            roman += encoder(int(number/100), 'C', 'D', 'M')
            number %= 100
        if number <= 99:
            roman += encoder(int(number/10), 'X', 'L', 'C')
            number %= 10
        if number <= 9:
            roman += encoder(number, 'I', 'V', 'X')
            number -= 9
        if number < 9:
            break
    print(roman)

    '''def encoder(num, let, nlet, number = number, roman = ''):  # seocond attempt
        if number <= num:
            for i in range(number):
                roman += let
        elif number == num + 1:
            number -= num
            for i in range(number):
                roman += let
            roman += nlet
        elif number <= num + num +2:
            number -= num+2
            roman += nlet
            for i in range(number):
                roman += let
        return roman

    if number <=8:  # seocond attempt
        roman += encoder(3, 'I', 'V')
    elif number <= 13:
        roman += encoder(8, 'I', 'X')
    elif number <= 18:
        roman += 'X'
        roman += encoder(13, 'I', 'V')
        #roman += encoder()
    elif number <= 23:
        roman += 'X'
        roman += encoder(18, 'I', 'X')
    elif number <= 28:
        roman += 'XX'
        roman += encoder(23, 'I', 'V')
    elif number <= 33:
        roman += 'XXX'
        roman += encoder(28, 'I', 'X')
    elif number <= 38:  # i dont think continuing like this is a good solution..
        roman += 'XXX'
        roman += encoder(33, 'I', 'V')
    elif number <= 43:
        roman += 'X'
        roman += encoder(38, 'I', 'L')

    print(roman)'''

''' #prototype 
if number <= 3:
    for i in range(number):
        roman += 'I'

elif number == 4:
    number -=3
    roman += 'V'
    for i in range(number):
        roman += 'I'

elif number <= 8:
    number -= 5
    for i in range(number):
        roman += 'I'
    roman += 'V'

elif number == 9:
    roman += 'IX'
elif number <= 13:
    number -= 10
    roman += 'X'
    for i in range(number):
        roman += 'I'''

