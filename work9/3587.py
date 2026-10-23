'''one two'''
n = int(input())

if n == 1:
    print("1")
elif n == 2:
    print("2")
else:
    s1 = "1"
    s2 = "2"
    for _ in range(3, n + 1):
        s_next = s2 + s1
        s1 = s2
        s2 = s_next
    print(s2)
