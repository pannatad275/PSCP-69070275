'''heron'''
import math as m
a = float(input())
b = float(input())
c = float(input())

s = (a + b + c)/2
d = s*(s - a)*(s - b)*(s - c)
Area = m.sqrt(d)
print(f"{Area:.3f}")
