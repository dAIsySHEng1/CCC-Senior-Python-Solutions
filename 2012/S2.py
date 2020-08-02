num = input()

def rmnumcalc(n):
    if n=='I':
        n = 1
    elif n=='V':
        n = 5
    elif n=='X':
        n = 10
    elif n=='L':
        n = 50
    elif n=='C':
        n = 100
    elif n=='D':
        n = 500
    else:
        n = 1000
    return n

s = int(num[-2])*rmnumcalc(num[-1])
i = 1
while i+2<=len(num):
    if int(rmnumcalc(num[i]))<int(rmnumcalc(num[i+2])):
        s -= int(num[i-1])*rmnumcalc(num[i])
    else:
        s += int(num[i-1]) * rmnumcalc(num[i])
    i += 2

print(s)
