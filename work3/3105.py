'''taxi'''
def main():
    '''taxi'''
    dis = int(input())
    x = 0
    for i in range(1,dis+1):
        if i <= 1:
            x += 35
            i+=1
        elif 1 < i <= 10:
            x += 5
            i+=1
        elif i > 10:
            x += 8
            i+=1
    print(x)
main()
