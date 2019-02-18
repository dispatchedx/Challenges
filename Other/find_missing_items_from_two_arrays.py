def reverse(string):
    """ Reverses a string in O(n) time and O(2n) ? space """
    string_length = len(string)
    reversed_string = [None] * string_length
    for c in string:
        reversed_string[string_length-1] = c
        string_length-=1
    return ''.join(reversed_string)


def find_missing(arr_string1,arr_string2):
    """ Returns the missing items (arr 2 is a part of arr 1) """
    arr_string1 = set(arr_string1)
    arr_string2 = set(arr_string2)
    return arr_string1-arr_string2
