#ZAD2
def max(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c

a = raw_input()
b = raw_input()
c = raw_input()
print max(a,b,c)