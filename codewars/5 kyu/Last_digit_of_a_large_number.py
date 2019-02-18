
def last_digit(n1, n2):
    """ Gets last digit of a large power """
    last_digit_dict = {  # Last digit cycles through a pattern
        0: [0],
        1: [1],
        2: [2,4,8,6],
        3: [3,9,7,1],
        4: [4,6],
        5: [5],
        6: [6],
        7: [7,9,3,1],
        8: [8,4,2,6],
        9: [9,1]
    }
    if n2 == 0:
        return 1
    lastd = n1 % 10                      # last digit of base
    pattern = last_digit_dict.get(lastd)    # corresponding pattern of the digit
    length_pattern = len(pattern)
    remainder = n2 % length_pattern           # divide exponent by the length of pattern
    return pattern[remainder-1]          # last digit of the operation is in list at index=remainder

''' usage: print(last_digit(2,2223))'''
