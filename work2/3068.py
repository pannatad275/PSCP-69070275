'''year'''
def main():
    '''year'''
    year = int(input())
    month = int(input())
    day = int(input())

    year2 = int(input())
    month2 = int(input())
    day2 = int(input())

    people1 = day
    for y in range(1, year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            people1 += 366
        else:
            people1 += 365

    for m in range(1, month):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            people1 += 31
        elif m in [4, 6, 9, 11]:
            people1 += 30
        elif m == 2:
            if (year % 4 == 0 and year % 100 != 0) or (y1 % 400 == 0):
                people1 += 29 
            else:
                people1 += 28

    people2 = day2
    for y in range(1, year2):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            people2 += 366
        else:
            people2 += 365

    for m in range(1, month2):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            people2 += 31
        elif m in [4, 6, 9, 11]:
            people2 += 30
        elif m == 2:
            if (year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0):
                people2 += 29 
            else:
                people2 += 28
    diff = abs(people1 - people2)
    
    if diff <= 7:
        print(0)
    elif people1 < people2:
        print(1)
    else:
        print(2)
main()
