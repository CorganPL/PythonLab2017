def flog(a):
    return a%2

def ftest(f, n):
    return [i for i in range(0, n+1) if f(i)]

print ftest(flog, 111)
