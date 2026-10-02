'''GCD_N'''
import math as m
def main():
    '''GCD_N'''
    n = int(input())
    ans = int(input())
    for _ in range(n-1):
        num = int(input())
        ans = m.gcd(ans,num)
    print(ans)
main()
