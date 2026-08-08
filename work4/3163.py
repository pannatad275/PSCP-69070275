'''pac'''
def main():
    '''pac'''
    n = int(input())
    sum1 = 0
    count_even = 0
    count_odd = 0
    for _ in range(n):
        num = int(input())
        sum1 += num
        if not num % 2:
            count_even += 1
        else:
            count_odd += 1
    print(f"SUM {sum1}")
    print(f"EVEN {count_even}")
    print(f"ODD {count_odd}")
main()
