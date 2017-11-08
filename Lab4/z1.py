def fun(napis):
    slownik={}
    for line in napis.splitlines():
        elementy = line.split(': ')
        slownik[elementy[0]] = elementy[1]

    print slownik.items()

nap = '''k1:w1
k2:w2
k3:w3'''

fun(nap)
