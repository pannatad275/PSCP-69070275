'''inflation'''
import math as m
def main():
    '''infration'''
    n = float(input())
    k = int(input())
    for _ in range(k):
        inc = n * 0.0381
        ans = m.floor(inc * 100 + 1e-9) /100
        n += ans
    print(f'{n:.2f}')
main()
