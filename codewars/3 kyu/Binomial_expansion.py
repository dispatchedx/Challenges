import math
def expand(expr):
    print(expr)
    for char in range(len(expr)):
        if expr[char] == "^":
            power = int(expr[char + 1:])
            expr = (expr[1:char - 1])
            break
    print(expr)
    if "+" in expr[1:]:
        term2sign = "+"
    else:
        term2sign = "-"

    if expr[0] == "-":
        term1sign = "-"
        expr = expr[1:]
    else:
        term1sign = ""
    term1, term2 = expr.split(term2sign)

    if power == 0:
        return '1'
    if power == 1:
        return term1sign + term1 + term2sign + term2

    term1variable = term1[-1]
    term1numeric = term1[:-1]

    if term1numeric == "":
        term1numeric = 1
    term1numeric_pow = str(pow(int(term1numeric), int(power)))
    if term1numeric_pow=='1':
        term1numeric_pow=""

    if int(power)%2==0:
        expr = "" + term1numeric_pow + term1variable + "^" + str(power)
    else:
        expr = term1sign + term1numeric_pow + term1variable + "^" + str(power)

    coefs=[]
    kappa=[]
    for k in range(int(power)):
        coefs.append(int(math.factorial(power) / (math.factorial(power - k) * math.factorial(k))))
        kappa.append("("+str(pow(int(term1sign+term1numeric), power-k))+")" + "(" + str(pow(int(term2sign+term2), k))+")")
    print(coefs)
    print(kappa)
    for i in range(int(power)-1, -1, -1):
        anti_i = int(power) - i
        term1numeric_pow = str(pow(int(term1numeric), i))
        term_2_pow = str(coefs[-i] * pow(int(term2), anti_i))
        if term1numeric_pow =='1' and term_2_pow == '1':
            term1numeric_pow = 0
            term_2_pow = 0

        if i == 0:
            if power%2==0:
                expr = expr + "+" + str(pow(int(term2), anti_i))
            else:
                expr = expr + "-" + str(pow(int(term2), anti_i))
            break
        if i%2==0:

            if term2sign =="-":
                expr = expr + "-" + str(int(term_2_pow) * int(term1numeric_pow)) + term1variable + "^" + str(i)
            else:
                expr = expr+"+" + str(int(term_2_pow)*int(term1numeric_pow)) + term1variable + "^" + str(i)
        else:
            if term1sign=="-":
                expr = expr+ "-" + str(int(term_2_pow)*int(term1numeric_pow)) + term1variable + "^" + str(i)
            else:
                expr = expr+ "+" + str(int(term_2_pow)*int(term1numeric_pow)) + term1variable + "^" + str(i)
        if i == 1:
            expr=expr[:-2]
    return expr

res= expand("(5m-3)^4")
print(res)