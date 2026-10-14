'''array'''
def main():
    '''array'''
    numbers = []

    for i in range(1, 4):
        value = int(input())
        numbers.append(value)
        print(f"Input number {i} stored.")

    while True:
        choice = int(input())
        if not choice:
            break
        if choice == 1:
            res = " ".join(map(str, numbers))
            print(f"Original order: {res}")
        elif choice == 2:
            desc = sorted(numbers, reverse=True)
            res = " ".join(map(str, desc))
            print(f"Descending order: {res}")
        elif choice == 3:
            asc = sorted(numbers)
            res = " ".join(map(str, asc))
            print(f"Ascending order: {res}")
main()
