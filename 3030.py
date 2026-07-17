'''saitama'''
def main():
    '''saitama'''
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    f = int(input())
    g = int(input())
    h = int(input())
    i = int(input())

    daya = a / f
    dayb = b / g
    dayc = c / h
    dayd = d / i

    min_day = max(daya, dayb, dayc, dayd)
    print(f"{min_day:.0f}")
main()