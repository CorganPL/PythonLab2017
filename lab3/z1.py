import math

class liczbaZespolona:
    a, b, mod = None, None, None
    def __init__(self, a, b):
        self.a, self.b, = a, b

    def __add__(self, other):
        return liczbaZespolona(self.a + other.a, self.b + other.i)

    def __sub__(self, other):
        return liczbaZespolona(self.a - other.a, self.b - other.i)

    def __mul__(self, other):
        return liczbaZespolona(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __div__(self, other):
        return liczbaZespolona(((self.a * other.a + self.b * other.b) / (math.pow(other.a, 2) + math.pow(other.b, 2)) )
                                + (((self.b * other.a - self.a * other.b) / (math.pow(other.a, 2) + math.pow(other.b, 2)))))

    def __str__(self):
        return ("%i + %ii" % (self.a, self.b))

    def modul(self):
        mod = math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2))


