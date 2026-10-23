'''list prime'''
n = int(input())
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            is_prime = False
            break
if is_prime:
    print("Yes")
    primes = []
    for num in range(2, n + 1):
        check = True
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                check = False
                break
        if check:
            primes.append(str(num))
    print(" ".join(primes))
else:
    print("No")
