'''bunny'''
a, b, c = input().split(" ")
price = int(input())

d = int(a)
e = int(b)
f = int(c)

fence = ((d*2) + (e*2))*f
All_price = fence*price
print(fence)
print(All_price)
