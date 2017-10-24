import os

def wyswPliki (path, ex):
    return [file for file in os.listdir(path) if ex in file]

sc = raw_input("Sciezka: ")
rozsz = raw_input("Rozszerzenie: ")

print (wyswPliki(sc, rozsz))
