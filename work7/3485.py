'''id'''
_ = int(input())
items = list(map(int, input().split()))

rare_items = []

for x in items:
    count_of_x = items.count(x)
    if count_of_x == 1:
        rare_items.append(x)

rare_items.sort()

print(*rare_items)
