def Fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif (n>1):
        return (Fib(n-1) + Fib(n-2))

x = int(raw_input())

i=1

while i<=x:
    print Fib(i)
    i+=1