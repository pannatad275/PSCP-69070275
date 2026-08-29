'''ticket'''
def main():
    '''ticket'''
    n = int(input())
    while n > 0:
        age,want_tic = map(int,input().split())

        if age < 15:
            print(-1)
            continue

        if want_tic > n:
            print(-2)
            continue

        prize = 150
        if 15 <= age <= 22:
            per = 80 / 100
        elif 22 < age < 60:
            per = 1
        else:
            per = 50 / 100

        n -= want_tic
        total = (prize * want_tic) * per
        print(f'{total:.0f} {n}')
main()
