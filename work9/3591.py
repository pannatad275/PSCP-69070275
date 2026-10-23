'''olympic'''
n = int(input())

countries = []
for _ in range(n):
    data = input().split()
    code = data[0]
    gold = int(data[1])
    silver = int(data[2])
    bronze = int(data[3])
    total = gold + silver + bronze
    countries.append((code, gold, silver, bronze, total))
countries.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
current_rank = 1

for i in range(n):
    code, gold, silver, bronze, total = countries[i]
    if i > 0:
        prev_country = countries[i - 1]
        prev_medals = (prev_country[1], prev_country[2], prev_country[3])
        curr_medals = (gold, silver, bronze)
        if curr_medals != prev_medals:
            current_rank = i + 1
    print(f"{current_rank} {code} {gold} {silver} {bronze} {total}")
