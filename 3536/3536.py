'''isprime'''
n = int(input())
if n <= 1:
    print("NO")
else:
    is_prime = True
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        if not n % i:
            is_prime = False
            break
    if is_prime:
        print("YES")
    else:
        print("NO")
