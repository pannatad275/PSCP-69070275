'''finov2'''
memo = {}
def fib(n):
    '''finov2'''
    if not n:
        return (0, 1)
    if n in memo:
        return memo[n]
    a, b = fib(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    if not n % 2:
        res = (c, d)
    else:
        res = (d, c + d)
    memo[n] = res
    return res
num = int(input())
print(fib(num)[0])
