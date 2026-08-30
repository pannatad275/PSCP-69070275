'''flower'''
def main():
    '''flower'''
    L,N = map(int,input().split())
    start = 1
    sum_n = 0
    while sum_n < N:
        sum_n += (start**2) * L
        if sum_n >= N:
            print(start)
            break
        start += 1
main()
