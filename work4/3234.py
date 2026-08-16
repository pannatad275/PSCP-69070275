'''chis'''
def main():
    '''chis'''
    x,n = input().split()
    n = int(n)
    start = 0
    li = ['Red','Green','Blue']
    if x == 'R':
        start = 0
    elif x == 'G':
        start = 1
    elif x == 'B':
        start = 2
    result = []
    for i in range(n):
        result.append(li[(start + i) % 3])
    print(*result)
main()
