import math

def pierw(a, b):
    try:
        b = float(1/b)
        res = math.pow(a, b)
    except (ZeroDivisionError, TypeError, ValueError) as ex:
        print ex
    else:
        print res

a = raw_input("Podaj podstawe: ")
b = raw_input("Podaj stopien pierwiastkowania: ")
print pierw(float(a), float(b))
