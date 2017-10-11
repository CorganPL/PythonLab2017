#ZAD3

n = int(raw_input())

i = 0
while i < 26:
    if (i%n == 0):
        print chr(ord('a') + i)
        print chr(ord('A') + i)
    i += 1