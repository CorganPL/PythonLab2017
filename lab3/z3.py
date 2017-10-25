import math

class Samochod(object):
    marka, pojemnoscBaku, predkoscMax, zuzyciePaliwa = None, None, None, None
    def __init__(self, mar, poj, pred, zuz):
        self.marka = mar
        self.pojemnoscBaku = poj
        self.predkoscMax = pred
        self.zuzyciePaliwa = zuz

    def aktualneZuzycie(self, predkosc):
        if (predkosc < self.predkoscMax):
            if (predkosc < int(self.predkoscMax*0.3) or predkosc > int(self.predkoscMax*0.8)):
                return self.zuzyciePaliwa*1.2
            else:
                return self.zuzyciePaliwa
        else:
            print "Przekroczono predkosc maksymalna"

    def jedz(self, predkosc, odleglosc):
            czasPodrozy = odleglosc/(predkosc*1.0)
            pelneZuzycie = (self.zuzyciePaliwa * odleglosc)/100
            ileTankowan = math.ceil(pelneZuzycie/self.pojemnoscBaku)

            print 'Predkosc: ', predkosc, 'km/h\nCzas podrozy: ', czasPodrozy, 'h \nZuzycie paliwa: ', \
                self.aktualneZuzycie(predkosc), 'l/100km \nIlosc tankowan: ', ileTankowan

class Kabriolet(Samochod):
    otwartyDach = None
    def __init__(self, mar, poj, pred, zuz):
        super(Kabriolet, self).__init__(mar, poj, pred, zuz)
        self.otwartyDach = False

    def otworzDach(self):
        if (self.otwartyDach == False):
            self.otwartyDach = True
        else:
            print 'Dach jest juz otwarty'

    def zamknijDach(self):
        if (self.otwartyDach == True):
            self.otwartyDach = False
        else:
            print 'Dach jest juz zamkniety'

    def aktualneZuzycie(self, predkosc):
        if (self.otwartyDach == True):
            return super(Kabriolet, self).aktualneZuzycie * 1.15
        elif(self.otwartyDach == False):
            return super(Kabriolet, self).aktualneZuzycie
        else:
            print "Przekroczono predkosc maksymalna"

kab = Kabriolet("X", 60, 190, 8)
sam = Samochod("X", 60, 190, 8)

print sam.aktualneZuzycie(120)
print kab.aktualneZuzycie(120)
