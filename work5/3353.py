'''pickthemagain'''
def main():
    '''101'''
    n = input().split()
    list1 = []
    for i in n:
        list1.append(int(i))
    ans = []
    for num in reversed(list1):
        if not num % 3 or not num % 5:
            ans.append(num)
    if not ans:
        print('Nope')
    else:
        for j in ans:
            print(j)
main()
