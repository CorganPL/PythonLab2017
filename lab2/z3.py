def fib_gen():
    p=0
    n=1
    yield p
    yield n

    while True:
        t = p + n
        p = n
        n = t
        yield n

f = fib_gen()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
