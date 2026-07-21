'''milk'''
def main():
    '''milk'''
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    buy = d // a
    total = buy
    caps = buy
    while caps >= b > 0:
        change = (caps // b) * c
        total += change
        caps = (caps % b) + change

    print(total)
main()
