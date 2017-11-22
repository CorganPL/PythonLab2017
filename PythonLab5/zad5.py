class Ksiazka:
    tytul="",
    numer=0,
    ISBN="",
    autor=""

    def __init__(self, tytul, numer, ISBN, autor):
        self.tytul=tytul
        self.numer=numer
        self.ISBN=ISBN
        self.autor=autor

class Biblioteka:
    ksiazki = []

    def dodaj(self, ksiazka):
        ksiazki.append(ksiazka)

    def usun(self, ksiazka):
        ksiazki.remove(ksiazka)

    def wypisz(self):
        print [ksiazka.tytul for ksiazka in ksiazki]

ksiazki = []

k1 = Ksiazka("Wladca Pierscieni", 2, "124-DDD", "J.R.R Tolkien")
k2 = Ksiazka("Mgly Avalonu", 1, "523-CCD", "Marion Bradley")

b = Biblioteka()
b.dodaj(k1)
b.dodaj(k2)
b.wypisz()
