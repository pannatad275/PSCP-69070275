'''castle'''
def main():
    '''castle'''
    N = int(input())
    floor = 1
    while floor**2 < N:
        floor += 1
    F = (floor**2) - N
    room = 2*(floor) - 1
    if not F % 2:
        print(room -1)
    else:
        print(room - 2)
main()
