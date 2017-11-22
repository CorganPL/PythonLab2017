def fun(plik):

    width = raw_input()
    width = int(width)

    napis = ''
    with open(plik, 'r') as f:
        napis = f.read()

    napis = napis.replace('\n', ' ')

    while napis:
        print napis[:width]
        napis = napis[:width]

    print napis.center(width)

fun("test.txt")
