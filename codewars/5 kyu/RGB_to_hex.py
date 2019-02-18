def rgb(r, g, b):
    lel = [r, g, b]
    result = ''
    for value in lel:

        if value > 255:
            value = 255
        elif value < 0:
            value = '00'
            result += value.upper()
            continue
        elif value < 9:
            value = '0' + str(value)
            result += value.upper()
            continue
        value = hex(int(value))[2:]
        result += value.upper()

    print(result)

rgb(0,0,0)
rgb(1,2,3)
rgb(255,255,255)
rgb(254,253,252)
rgb(-20,275,125)