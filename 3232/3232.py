'''frog'''
def main():
    '''frog'''
    x, y = map(int,input().split())
    total_dis = 0
    count = 0
    reach = False
    while x > 0:
        total_dis += x
        count += 1
        if total_dis >= y:
            reach = True
            break
        x -= 2
    if reach:
        print(count)
    else:
        print(-1)
main()
