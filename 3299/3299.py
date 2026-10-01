'''flower'''
def main():
    '''flower'''
    L,N = map(int,input().split())
    diag = 1
    while N > 0:
        N -= diag
        if N <= 0:
            break
        diag += 1
    ans = (diag - 1) // L + 1
    print(ans)
main()
