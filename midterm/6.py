'''6'''
def main():
    '''6'''
    n = float(input())
    w1 = input()
    w2 = input()
    x = 0
    y = 0
    if w2 == 'NIU':
        x = n * 1
    elif w2 == 'KUEP':
        x = n * 12
    elif w2 == 'SOK':
        x = n * 24
    elif w2 == 'WA':
        x = n * 96
    elif w2 == 'SEN':
        x = n * 1920

    if w1 == 'NIU':
        y = x
    elif w1 == 'KUEP':
        y = x /12
    elif w1 == 'SOK':
        y = x /24
    elif w1 == 'WA':
        y = x/96
    elif w1 == 'SEN':
        y = x/1920
    print(f'{y:.4f}')
main()
