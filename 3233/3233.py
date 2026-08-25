'''hu'''
def main():
    '''hu'''
    al1,n1 = input().split()
    al2,n2 = input().split()
    if al1 == al2 and n1 == n2:
        get = 1000000
    elif n1 == n2 and al1 != al2:
        get = 100000
    elif n1[2:5] == n2[2:5] and al1 == al2:
        get = 2000
    elif n1[3:5] == n2[3:5] and al1 == al2:
        get = 1000
    elif n1[2:5] == n2[2:5] and al1 != al2:
        get = 200
    elif n1[3:5] == n2[3:5] and al1 != al2:
        get = 100
    elif al1 == al2 and n1 != n2:
        get = 20
    else:
        get = 0
    print(get)
main()
