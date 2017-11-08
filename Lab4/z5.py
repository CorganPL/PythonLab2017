def zaszyfruj(plikWe, plikWy):
    wartosc = raw_input("Wartosc szyfrowania: ")
    with open(plikWe, 'r') as f:
            tresc = f.read()

    szyfrogram = ''

    for i in range(len(tresc)):
       if ord(tresc[i]) > 122 - wartosc:
           szyfrogram += chr(ord(tresc[i]) + wartosc - 26)
       else:
           szyfrogram += chr(ord(tresc[i]) + wartosc)

    with open(plikWy, "w") as f:
        f.write(szyfrogram)

zaszyfruj("test.txt", "szyfrogram.txt")
