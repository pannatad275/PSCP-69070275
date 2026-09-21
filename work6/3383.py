'''diff'''
def main():
    '''diff'''
    n = int(input())
    m = int(input())
    nA = set()
    for _ in range(n):
        nA.add(int(input()))
    mB = set()
    for _ in range(m):
        mB.add(int(input()))
        diff = nA - mB
    print(*sorted(diff))
main()
