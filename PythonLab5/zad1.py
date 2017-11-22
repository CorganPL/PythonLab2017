def fun(plik):

    width = raw_input()

    napis = ''
    with open(plik, 'r') as f:
        napis = f.read()

    napis = napis.replace('\n', ' ')

    while napis:
        print napis[:width]
        napis = napis[:width]

fun("test.txt")
