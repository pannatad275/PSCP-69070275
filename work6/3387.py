'''tuple'''
def main():
    '''tuple'''
    n = tuple(input().split())
    tar = input()
    idx = n.index(tar)
    cnt = n.count(tar)
    row = " ".join([str(idx)] * cnt)
    for _ in range(cnt):
        print(row)
main()
