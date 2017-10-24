import math

def odl(x1, y1, x2, y2):
    return ( math.sqrt( pow(x2-x1, 2) + pow(y2-y1, 2)))

def fun(punkty, kon):
    return [(punkty[i][0], punkty[i][1], odl(punkty[i][0],punkty[i][1],kon[0],kon[1])) for i in len(punkty)]

points = [(1,2), (3,10), (0,4)]
xc, xy = 3, 3
pkt = (xc, xy)

print fun(points, pkt)
