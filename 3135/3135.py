'''present'''
def main():
    '''present'''
    N,K,T = map(int,input().split())
    if T == 1:
        print(1)
    else:
        count = 0
        people = 1
        while True:
            count += 1
            if people == T:
                break
            people += K
            if people > N:
                people %= N
                if not people:
                    people = N
            if people == 1:
                break
        print(count)
main()
