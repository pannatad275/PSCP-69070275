'''inflation'''
def main():
    '''inflation'''
    n = float(input())
    k = int(input())
    rate = 0.0381
    for _ in range(k):
        inc = n * rate
        ans = int(inc * 100 + 1e-9) /100
        n += ans
    print(f'{n:.2f}')
main()
