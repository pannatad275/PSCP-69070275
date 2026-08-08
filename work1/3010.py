'''quad'''
a = int(input())
b = int(input())

if not a and not b:
    print("O")
elif not b:
    print("X")
elif not a:
    print("Y")
elif a > 0 and b > 0:
    print("Q1")
elif a < 0 < b:
    print("Q2")
elif a < 0 and b < 0:
    print("Q3")
else:
    print("Q4")
