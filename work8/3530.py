'''SqFree'''
n = int(input())

count = 0

for i in range(1, n + 1):
    is_square_free = True
    b = 2
    while b * b <= i:
        if not i % (b * b):
            is_square_free = False
            break
        b += 1
    if is_square_free:
        count += 1

print(count)
