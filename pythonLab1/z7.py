tresc = raw_input("Wyraz: ")
szyfrogram = []
x = raw_input('Wartosc szyfrowania')

list(tresc)

i=0
while i < len(tresc):
    szyfrogram.append(chr(ord(tresc[i]) + x))
    i+=1

print szyfrogram
