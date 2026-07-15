'''season'''

month = int(input())
day = int(input())

if month in [1, 2, 3]:
    if month % 3 == 0 and day >= 21:
        print("string")
    elif month % 3 != 0:
        print("winter")
elif month in [4, 5, 6]:
    if month % 3 == 0 and day >= 21:
        print("summer")
    elif month % 3 != 0:
        print("spring")
elif month in [7, 8, 9]:
    if month % 3 == 0 and day >= 21:
        print("fall")
    elif month % 3 != 0:
        print("summer")
elif month in [10, 11, 12]:
    if month % 3 == 0 and day >= 21:
        print("winter")
    elif month % 3 != 0:
        print("fall")
