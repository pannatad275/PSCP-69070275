'''saitama'''
import math as m
def main():
    '''saitama'''
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = int(input())
    h = int(input())
    if  min(a, b, c, d , e, f , g, h) > 0:
        daya = m.ceil(a / e)
        dayb = m.ceil(b / f)
        dayc = m.ceil(c / h)
        dayd = m.ceil(d / g)
        min_day = max(daya, dayb, dayc, dayd)
    else:
        min_day = 0

    print(min_day)
main()
