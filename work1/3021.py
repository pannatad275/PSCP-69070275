'''circle'''
import math as m

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

d = (x2 - x1)**2 + (y2 - y1)**2
dis = m.sqrt(d)
total_rad = r1+r2

if dis <= total_rad:
    print("overlapping")
else:
    print("no overlapping")
