'''game point'''
point = int(input())
bonus = int(input())
day = int(input())
NO = 0
if day > 3:
    total_point = (point + bonus)*1.5
else:
    total_point = point + bonus
if total_point < 200:
    NO = 1
elif total_point >= 1500:
    NO = 5
elif total_point >= 1000:
    NO = 4
elif total_point >= 500:
    NO = 3
elif total_point >= 200:
    NO = 2

if NO == 5 and day >= 7:
    PASSWORD = 99
elif NO == 4 and bonus > 300:
    PASSWORD = 88
else:
    PASSWORD = 0
print(int(total_point))
print(NO)
print(PASSWORD)
