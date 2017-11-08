def fun(plik):
    napis = ''
    with open(plik, 'r') as f:
        napis = f.read()

    slownik={}
    for line in napis.splitlines():
        elementy = line.split(': ')
        slownik[elementy[0]] = elementy[1]

    print slownik.items()

fun("test.txt")
