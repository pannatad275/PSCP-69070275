'''1'''
def main():
    '''1'''
    n = int(input())
    n1 = int(input())
    low_n = n1
    max_n = n1
    total_n = n1
    for _ in range(n-1):
        n2 = int(input())
        if n2 < low_n:
            low_n = n2
        elif n2 > max_n:
            max_n = n2
        total_n += n2
    avg = total_n / n
    print(f'MIN: {low_n:.3f}')
    print(f'MAX: {max_n:.3f}')
    print(f'AVG: {avg:.3f}')
main()
