'''dup'''
def main():
    '''dup'''
    m = int(input())
    n = int(input())
    id1 = []
    id2 = []
    for _ in range(m):
        st_id1 = int(input())
        id1.append(st_id1)
    for _ in range(n):
        st_id2 = int(input())
        id2.append(st_id2)
    for i in id1:
        for j in id2:
            if i == j:
                print(i)
            else:
                print('Nope')
main()
