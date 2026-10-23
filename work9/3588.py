'''fibo'''
def fib(n):
    '''fibo'''
    if not n:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
num = int(input())
print(fib(num))
