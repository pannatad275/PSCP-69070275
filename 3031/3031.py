'''Ink'''
import math as m
def main():
    '''Ink'''
    pi = 3.1416
    S, N = map(int,input().split())
    for _ in range(N):
        X, Y = map(int,input().split())
        #area = pi*r**2
        #r**2 = X**2 + Y**2
        area = pi * (X**2 + Y**2)
        s = m.ceil(area / S)
        print(s)
main()
