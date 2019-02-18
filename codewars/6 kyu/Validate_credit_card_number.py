def validate(n):
    digits = list(map(int, list(str(n))))[::-1]

    for i in range(1, len(digits), 2):
        if digits[i] >= 5:
            digits[i] = digits[i] * 2 - 9
        else:
            digits[i] = digits[i] * 2
    fsum = sum(digits)
    if fsum % 10 == 0:
        return True
    else:
        return False