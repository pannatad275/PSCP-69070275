'''Pro'''
x = int(input())
y = int(input())
a = int(input())
z = int(input())

if z >= x:
    print((((z // x) * y) + (z % x)) * a)
else:
    print(a * z)
