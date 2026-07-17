'''money'''
def main():
    '''money'''
    money = int(input())

    x = money // 10
    money %= 10

    y = money // 5
    money %= 5

    z = money // 2
    money %= 2

    v = money // 1

    print(f"10 = {x}")
    print(f"5 = {y}")
    print(f"2 = {z}")
    print(f"1 = {v}")

main()