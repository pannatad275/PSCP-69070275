'''k'''
def main():
    '''d'''
    n = int(input())
    list1 = []
    for _ in range(n):
        num = int(input())
        list1.append(num)
    max_count = 0
    for i in list1:
        count = list1.count(i)
        if count > max_count:
            max_count = count
    print(max_count)
main()
