#ZAD5

n = int(raw_input())

lista = []

i=0
while i<n:
    x = raw_input()
    lista.append(x)
    i+=1

kier = raw_input("L/P?")

if(kier == 'L'):
    lista.sort()
elif(kier == "P"):
    lista.sort(reverse = True)

m = int(raw_input())

j=0
while j<m:
    print lista[j]
    j+=1
