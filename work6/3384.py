'''pickthem'''
def main():
    '''pick'''
    n = input()
    num = n[1:-1].split(',')
    even_num = []
    for i in num:
        num1 = int(i.strip())
        if not num1 % 2:
            even_num.append(num1)
    if len(even_num) > 0:
        for j in even_num:
            print(j)
    else:
        print('Nope')
main()
