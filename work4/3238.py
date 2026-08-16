'''elon mask'''
def main():
    '''elon mask'''
    x,k = input().split()
    x = int(x)

    cen = x // 2
    for i in range(x):
        if k == '#':
            p = '#'
        else:
            diff = abs(i - cen)
            p = chr(ord(k) + diff)
        for j in range(x):
            if i == j or i + j == x - 1:
                print(p, end='')
            else:
                print('-', end='')
        print()
main()
