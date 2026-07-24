'''brick'''
def main():
    '''brick'''
    smallb = int(input())
    bigb = int(input())
    goal = int(input())
    use_bigb = min(bigb, goal // 5)
    need_smallb = goal - (use_bigb * 5)
    if smallb >= need_smallb:
        print(need_smallb)
    else:
        print(-1)
main()
