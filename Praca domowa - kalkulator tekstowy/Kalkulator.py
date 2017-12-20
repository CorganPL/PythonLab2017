#dzialanie = raw_input()
#print eval(dzialanie)
#Te dwie linijki wyzej zalatwilyby wszystko, ale domyslam sie, ze nie o to chodzilo

priorytet = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

operatory = ['+', '-', '*', '/']
cyfry = ['0, ''1', '2', '3', '4', '5', '6', '7', '8', '9',
         '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']

#zamiennik isdigit sprawdzajacy takze czy jset to liczba ujemna
def czyLiczba(liczba):
    list(liczba)
    if(str(liczba[0]).isdigit() or (str(liczba[0] == '-') and len(liczba) > 1)):
        i=1
        while(i<len(liczba)):
            if(not liczba[i].isdigit()):
                return False
            i+=1
        return True
    return False

def zamienNaONP(dzialanie):
    dzialanie = list(dzialanie)
    dzialanie = ['('] + dzialanie + [')']

    #konkatenacja cyfr
    i=0
    while(i < len(dzialanie)-1):
        while (not dzialanie[i] in cyfry and i < len(dzialanie)-1):
            if (dzialanie[i] == '(' and dzialanie[i+1] == '-'):             #wykrywanie liczb ujemnych
                dzialanie[i+2] = str(dzialanie[i+1]) + str(dzialanie[i+2])
                del dzialanie[i+1]
            i+=1
        if (i == len(dzialanie)-1):
            break
        while(dzialanie[i+1].isdigit()):
            dzialanie[i] += str(dzialanie[i+1])
            del dzialanie[i+1]
        i+=1

    wyjscie, stos = [], []

    for i in dzialanie:
        if (i == '('):
            stos.append(i)

        if (i == ')'):
            while(stos[-1] != '('):
                wyjscie.append(stos[-1])
                stos.pop()
            stos.pop()

        if (i in operatory):
            while(len(stos) > 0):
                if (priorytet.get(i) > priorytet.get(stos[-1])):
                    stos.append(i)
                    break
                else:
                    wyjscie.append(stos[-1])
                    stos.pop()

        if (czyLiczba(i)):
            wyjscie.append(i)

    return wyjscie

def wyliczONP(dzialanie):

    v1, v2 = None, None
    stos = []

    for i in dzialanie:
        if (czyLiczba(i)):
            stos.append(i)
        if (i in operatory):
            v2 = stos.pop()
            v1 = stos.pop()

            v1, v2 = float(v1), float(v2)
            if (i == '+'):
                v1 = v1+v2
            if (i == '-'):
                v1 = v1-v2
            if (i == '*'):
                v1 = v1*v2
            if (i == '/'):
                v1 = v1/v2

            stos.append(v1)

    return stos[0]

dzialanie = raw_input()
print wyliczONP( zamienNaONP(dzialanie))
