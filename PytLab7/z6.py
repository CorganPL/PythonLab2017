def jednosc(n):
    liczba = ""
    x = list(str(n))

    if(x[len(x)-1] == '1'):
        liczba += " jeden"
    if(x[len(x)-1] == '2'):
        liczba += " dwa"
    if(x[len(x)-1] == '3'):
        liczba += " trzy"
    if(x[len(x)-1] == '4'):
        liczba += " cztery"
    if(x[len(x)-1] == '5'):
        liczba += " piec"
    if(x[len(x)-1] == '6'):
        liczba += " szesc"
    if(x[len(x)-1] == '7'):
        liczba += " siedem"
    if(x[len(x)-1] == '8'):
        liczba += " osiem"
    if(x[len(x)-1] == '9'):
        liczba += " dziewiec"

    return liczba

def slownie(n):
    liczba = ""
    x = list(str(n))
    if (len(x) == 2):
        liczba += jednosc(x[0]) + "dziesiat" + jednosc(x[1])

    if (len(x) == 3):
        liczba += jednosc(x[0]) + "set" + jednosc(x[1]) + "dziesiat" + jednosc(x[2])

    return liczba

print slownie(572)
