import math
import re
def expand(expr):
    print(expr)
    # remove parenthesis and split expression into the 2 terms and exponent
    expr = re.findall('(-?\d*[a-z])([-+]\d*)\)\^(\d*)', expr)
    term1 = expr[0][0]
    term2 = expr[0][1]
    power = int(expr[0][2])
    print(expr, power)

    # edge cases
    if power == 0:
        return '1'
    if power == 1:
        return term1 + term2

    # split 1st term into numeric_part and variable parts
    term1variable = term1[-1]
    term1numeric = term1[:-1]

    #more edge cases
    if term1numeric == '':
        term1numeric = '1'
    elif term1numeric == '-':
        term1numeric = '-1'

    term1numeric_pow = str(pow(int(term1numeric), power))
    if term1numeric_pow == '1':
        term1numeric_pow = ''
    elif term1numeric_pow == '-1':
        term1numeric_pow = '-'
    # calculate first term of binomial expansion
    # (its done outside the loop to have the redundant "+" removed efficiently)
    expr = term1numeric_pow + term1variable + "^" + str(power)

    # calculate the rest of the binomial expansion
    for k in range(1, int(power+1)):
        coefficient = (int(math.factorial(power) / (math.factorial(power - k) * math.factorial(k))))
        term_product = (pow(int(term1numeric), power-k) * pow(int(term2), k))
        numeric_part = (coefficient*term_product)

        # this adds a "+" to positive terms
        if numeric_part > 0:
            numeric_part = "+" + str(numeric_part)
        else:
            # negative terms already have a "-" so no need to do anything
            numeric_part = str(numeric_part)

        # remove "1" from variables being multiplied by 1 ("1x+5" -> "x+5")
        if numeric_part == '+1':
            numeric_part = "+"
        elif numeric_part == '-1':
            numeric_part = '-'

        # combine all parts of a term and append to the expression
        expr = expr + numeric_part + term1variable + "^" + str(power-k)

    # this is to remove unnecessary ^1 from pre-last term
    expr = expr.replace("^1", "")

    # removes unnecessary var^0 from last term
    expr = expr.replace(f"{term1variable}^0", "")
    if expr[-1].isnumeric():
        return expr
    else:
        return expr+'1'


res = expand("(x+1)^2")
print(res)