import math
import pdb

class Punkt2D(object):
    x, y = None, None
    def __init__(self, x, y):
        pdb.set_trace()
        self.x, self.y = x, y

    def odleglosc(self, other):
        pdb.set_trace()
        return math.sqrt( math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2))

class Punkt3D(Punkt2D):
    z = None
    def __init__(self, x , y, z):
        pdb.set_trace()
        super(Punkt3D, self).__init__(x, y)
        pdb.set_trace()
        self.z = z

    def odleglosc(self, other):
        pdb.set_trace()
        return math.sqrt( math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2) )

p1 = Punkt2D(2, 1)
p2 = Punkt2D(3, 3)
print p1.odleglosc(p2)

p3 = Punkt3D(6, 1, 3)
p4 = Punkt3D(0, 1, 5)
print p3.odleglosc(p4)
