'''cokev2'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if not b or c >= a or d <= b:
    total = d * a
else:
    total = b * a + c
    rem = d - (b + 1)
    blocks = rem // b
    leftover = rem % b
    total += blocks * ((b - 1) * a + c)
    total += leftover * a
print(total)
