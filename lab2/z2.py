def fib(n):
    wyrazy = []
    wyrazy.append(1)
    wyrazy.append(1)
    return [wyrazy.append(wyrazy[k-2] + wyrazy[k-1]) for k in range(2,n)]

print fib(12)
