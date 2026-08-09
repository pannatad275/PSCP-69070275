'''point'''
def main():
    '''point'''
    n = int(input())
    point = 0
    for _ in range(n):
        s = input()
        if s == '+':
            point += 10
        else:
            point -= 5
    print(point)
main()
