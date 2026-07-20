'''coke'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())

total = 0
cap = 0

if not b:
    total = a * d
else:
    for i in range(d):
        i += 0
        if cap >= b:
            total += c
            cap -= b
        else:
            total += a
        cap += 1

print(total)
