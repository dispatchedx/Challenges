import re


def find_nested_parenthesis(string):
    """Removes parenthesis in an efficient way
    Args:
        string (str): parenthesis expression ex: "(2 / (2 + 3.33) * 4) - -6"
    Return:
        start (int), end (int), string (str): indexes of original string where parenthesis sub expression was found
        and the sub expression without the parenthesis
    """
    parenthesis_balance = 0
    start = None
    for i, ch in enumerate(string):
        if ch == "(":
            parenthesis_balance += 1
            if start is None:
                start = i
        elif ch == ")":
            parenthesis_balance -= 1
            if parenthesis_balance == 0:
                substring = string[start : i + 1]
                return start, i + 1, substring
    return None, None, None


def split_expressions(string: str) -> float:
    """Splits an expression into smaller parts, and returns the final calculated result
    Args:
        string (str): expression with potentially nested parenthesis ex: "(2 / (2 + 3.33) * 4) - -6"
    Returns:
        float: final calculated result
    """
    start, end, substring = find_nested_parenthesis(string)
    if substring:
        sub_exp = substring[1:-1]
        result = split_expressions(sub_exp)

        # check if theres a minus before the parenthesis
        has_minus_before = start > 0 and string[start - 1] == "-"

        if has_minus_before:
            # check what comes before the minus skipping spaces
            check_pos = start - 2
            while check_pos >= 0 and string[check_pos] == " ":
                check_pos -= 1

            # if theres an operator or we are at the start, its a negative sign
            if check_pos < 0 or string[check_pos] in "+-*/(":
                # remove the minus and negate result
                evaluated = string[: start - 1] + str(-result) + string[end:]
            else:
                # replace - with + and negate result
                evaluated = string[: start - 1] + "+" + str(-result) + string[end:]
        else:
            evaluated = string[:start] + str(result) + string[end:]

        return split_expressions(evaluated)
    else:
        return evaluate_cleaned(string)


def evaluate_cleaned(string: str) -> float:
    """takes a cleaned string of operations with no parenthesis and evaluates the result ex: "1 * 3 / 3 + 4 * -2 - -2"

    Args:
        string (str): cleaned string

    Returns:
        result(int): result of expression
    """
    # add whitespace between operators and operands
    string = re.sub(r"([*/+])", r" \1 ", string)
    string = re.sub(r"(\d)-", r"\1 -", string)

    # string = re.sub(r"--", r"+ ", string)
    # string = re.sub(r"(\d+.?\d*.+[\/*+])\s+[^\d]\+\s+(\d+.?\d+)", r"\1 \2", string)
    # string = re.sub(r"(\d+.?\d*.+[-+])\s+[^\d]\s+(\d+.?\d+)", r"\1 \2", string)
    # string = re.sub(r"(\d+.?\d*.+[-])\s+[+]\s+(\d+.?\d*)", r"\1 \2", string)
    # string = re.sub(r"(\d+.?\d*.+[-])\s+[-]\s+(\d+.?\d+)", r"\1 + \2", string)
    # string = re.sub(r"(\d+.?\d*.+[+])\s+[-]\s+(\d+.?\d+)", r"\1 - \2", string)
    # string = re.sub(r"(\d+.?\d*.+[-+])\s+[^\d]\s+(\d+.?\d+)", r"\1 \2", string)

    # split into parts
    arr = string.split()
    i = 0
    result = 0
    if len(arr) == 1:  # maybe <=2
        return float(arr[0])

    # first search for * and / and evaluate those, replacing the previous string
    while i < len(arr):
        if arr[i] == "*":
            result = float(arr[i - 1]) * float(arr[i + 1])
            arr[i - 1 : i + 2] = [str(result)]
            i -= 1
        elif arr[i] == "/":
            result = float(arr[i - 1]) / float(arr[i + 1])
            arr[i - 1 : i + 2] = [str(result)]
            i -= 1
        i += 1
    i = 0
    # then search for + and - and evaluate the final result
    while i < len(arr):
        if arr[i] == "+":
            result = float(arr[i - 1]) + float(arr[i + 1])
            arr[i - 1 : i + 2] = [str(result)]
            i -= 1
        elif arr[i] == "-":
            result = float(arr[i - 1]) - float(arr[i + 1])
            arr[i - 1 : i + 2] = [str(result)]
            i -= 1
        i += 1
    return result


test1 = "(2 / (2 + 3.33) * 4) - -6"
test2 = "1 + 3"
test3 = "1 * 3 / 3 + 4 * -2 - -2"
test4 = "8/16"
test5 = "3 -(-1)"
test6 = "(((10)))"
testx = "-(67) / (39 - 83 * -(67)) + (-32 / (((-(-84 + -79)))) / 67)"
testx = "(-32) * (-81 / -32 * -(62)) + (-53 / -((((-89 - -22)))) / 86)"
test9 = "-(10) * (48 * -83 - -(75)) * (78 * -(((-(-17 + 36)))) + -69)"
test10 = "(14) + (-6 * -68 / -(75)) * (93 + -(((-(36 + 43)))) / -18)"
test11 = "(2) + (50 * 36 * -(1)) / (-82 - -((((-87 - 45)))) / -6)"


# Test cases
test_cases = [
    ("-(67) / (39 - 83 * -(67)) + (-32 / (((-(-84 + -79)))) / 67)", "-0.012270124895437054"),
    ("(-32) * (-81 / -32 * -(62)) + (-53 / -((((-89 - -22)))) / 86)", "3937.009174311927"),
    ("-(10) * (48 * -83 - -(75)) * (78 * -(((-(-17 + 36)))) + -69)", "-2890440.0"),
    ("(14) + (-6 * -68 / -(75)) * (93 + -(((-(36 + 43)))) / -18)", "1334.7466666666667"),
    ("(2) + (50 * 36 * -(1)) / (-82 - -((((-87 - 45)))) / -6)", "-19.77777777777778"),
    ("(((-5))) + (((10)))", "5.0"),
    ("-(-(-(-(5))))", "5.0"),
    ("(((2 + 3))) * (((4 - 1)))", "15.0"),
    ("((10 / (2 + 3))) * ((4 * (5 - 2)))", "24.0"),
    ("-(((50))) + (((-(-(25)))))", "-25.0"),
    ("(-(5) * -(3)) + (-(2) / -(4))", "15.5"),
    ("((((((6))))))) * ((((((7))))))", "42.0"),
    ("-(((10 + 20))) / (((5 - 2)))", "-10.0"),
    ("(50) - (((30 + (10 * (2 + 3)))))", "-30.0"),
    ("((10)) * ((20)) + ((30)) / ((5))", "206.0"),
    ("-(((-(((5 + 3))))))", "8.0"),
    ("(((2))) * (((3))) + (((4))) - (((1)))", "9.0"),
    ("((((10 / 2)))) * ((((5 - 3))))", "10.0"),
    ("-(100) + (((50 * 2))) - (((-(-(25)))))", "-25.0"),
    ("(((((1 + 1))))) * (((((2 + 2))))) * (((((3 + 3)))))", "48.0"),
    ("((10 * (5 + (3 * (2 - 1)))))", "80.0"),
    ("-(((20 / (2 + 2)))) + (((30 * (1 + 1))))", "55.0"),
    ("(((100))) / (((-(-(10))))) + (((-(5))))", "5.0"),
]

# Run tests
for input_str, expected in test_cases:
    result = split_expressions(input_str)
    status = "✓" if result == expected else "✗"
    print(f"{status} '{input_str[:50]}...' -> {result}")
    if result != expected:
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
print(split_expressions(test11))
