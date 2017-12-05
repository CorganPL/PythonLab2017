import math

def rozklad(n):
    k = 2
    j = math.floor(math.sqrt(n))
    roz = []
    kr = ()
    pow = 0
    while(k<=j):
        if (n%k==0):
            roz.append(k)
            n/=k
            pow+=1
            j = math.floor(math.sqrt(n))
        else:
            roz.append(pow)
            kr[0] = k
            kr[1] = pow
            roz.append(kr)
            k+=1
            pow = 0

    if (n>1):
        kr[0] = k
        kr[1] = pow
        roz.append(kr)
        pow = 0

    return roz

print rozklad(756)
