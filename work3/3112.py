'''milktea'''
def main():
    '''milktea'''
    line1 = input().strip().split()
    a = line1[0].upper()
    b = int(line1[1])

    line2 = input().strip().split()
    c = line2[0].upper()
    d = int(line2[1])
    e = int(line2[2])

    cal_p = 0
    cal_tea = 0

    if a == "H":
        cal_p = 5 * b
    elif a == "O":
        cal_p = 3 * b
    elif a == "J":
        cal_p = 2 * b

    if c == "R":
        if d == 1:
            cal_tea = 12 * e
        elif d == 2:
            cal_tea = 18 * e
        elif d == 3:
            cal_tea = 25 * e
    elif c == "T":
        if d == 1:
            cal_tea = 15 * e
        elif d == 2:
            cal_tea = 20 * e
        elif d == 3:
            cal_tea = 30 * e
    elif c == "M":
        if d == 1:
            cal_tea = 10 * e
        elif d == 2:
            cal_tea = 15 * e
        elif d == 3:
            cal_tea = 20 * e
    print(cal_p + cal_tea)
main()
