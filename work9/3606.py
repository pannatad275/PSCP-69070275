'''ball'''
ss= float(input())
count = 0
while ss * 0.6 >= 0.01:
    ss *= 0.6
    count += 1
print(count)
