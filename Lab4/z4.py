def fun(plik, ciag):
    if (plik != '-'):
        with open(plik, 'r') as f:
            napis = f.read()
    else:
        while True:
            napis = raw_input()
            if napis == "":
                break

    for line in napis.splitlines():
        if ciag in line:
            print line

fun("test.txt", "dupa")




