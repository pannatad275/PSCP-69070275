'''bird'''
def main():
    '''bird'''
    n = int(input())
    h = list(map(int, input().split()))

    if n == 1:
        print(1)
        return

    count = 0

    for i in range(n):
        if not i:
            if h[i] > h[i + 1]:
                count += 1
        elif i == n - 1:
            if h[i] > h[i - 1]:
                count += 1
        else:
            if h[i] > h[i - 1] and h[i] > h[i + 1]:
                count += 1
    print(count)
main()
