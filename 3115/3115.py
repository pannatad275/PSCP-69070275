'''store check'''
def main():
    '''store check'''
    num,check = map(int,input().split())
    start1 = []
    stop1 = []
    count = 0
    for _ in range(num):
        start,stop = map(int,input().split())
        start1.append(start)
        stop1.append(stop)
    come = input().split()
    result = []
    for i in range(check):
        k = int(come[i])
        count = 0
        #print(come)
        for j in range(num):
            if start1[j] <= k < stop1[j]:
                count += 1
        result.append(str(count))
    print(" ".join(result))
main()
