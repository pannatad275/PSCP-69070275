'''car'''
def main():
    '''car'''
    n = int(input())
    v_list = []
    for _ in range(n):
        _, v = map(int, input().split())
        v_list.append(v)
    unsellable = 0
    max_v = 0
    for v in reversed(v_list):
        if v < max_v:
            unsellable += 1
        else:
            max_v = v
    print(unsellable)
main()
