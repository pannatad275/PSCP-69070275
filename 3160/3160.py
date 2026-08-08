'''wda'''
def main():
    '''dwa'''
    n1,n2 = map(int,input().split())
    num = []
    for i in range(n1,n2+1):
        if i >= 2:
            count = 0
            for j in range(1,i+1):
                if not i % j:
                    count += 1
            if count == 2:
                num.append(i)
    if len(num) > 0:
        print(*num)
    print(f"Total primes: {len(num)}")
main()
