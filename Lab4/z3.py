def fun(plik):
    with open(plik, 'r') as f:
        napis = f.read()

    slowa = napis.split()
    unikaty = sorted(set(slowa))

    slownik = {}

    for i in unikaty:
        slownik[i] = slowa.count(i)

    print slownik

fun("test.txt")
