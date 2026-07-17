'''min'''
def main():
    '''min'''
    n = int(input())
    low = int(input())
    for _ in range(n-1):
        num = int(input())
        if num < low:
            low = num
    print(low)
main()
