'''ts'''
def main():
    '''ts'''
    N = int(input())
    A = int(input())
    if not N or not N*A:
        print("No teaching")
    else:
        time = N * A
        hour = time // 60
        mins = time % 60
        if not mins:
            print(f'{hour} hours')
        elif not hour:
            print(f"{mins} minute")
        else:
            print(f'{hour} hours {mins} minute')
main()
