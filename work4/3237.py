'''tra'''
def main():
    '''tra'''
    n = int(input())
    if n > 0:
        for i in range(n):
            if not i:
                print('0')
            elif i == n - 1:
                print('0' * n)
            else:
                print('0' + '1' * (i - 1) + '0')
main()
