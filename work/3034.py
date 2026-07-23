'''pod'''
def main():
    '''pod'''
    N, K = map(int,input().split())
    line = []
    people = []
    people_line = []
    x = 0
    left = 0
    for i in range(1,K+1):
        line.append(i)
    for _ in range(N):
        p = int(input())
        people.append(p)
    for m in range(K):
        for n in range(N):
            if line[m] == people[n]:
                x += 1
        people_line.append(x)
        x = 0
    X = min(people_line)
    for v in range(K):
        people_line[v] -= X
    for c in range(K):
        left += people_line[c]
    print(left)
main()
