'''x'''
def main():
    '''x'''
    n,k = input().split()
    n = int(n)
    cen = n // 2
    for i in range(n):
        if k == '#':
            p = '#'
        else:
            diff = abs(i - cen)
            p = chr(ord(k) + diff)
        for j in range(n):
            if i == j or i + j == n - 1:
                print(p,end='')
            else:
                print('-',end='')
        print()
main()
