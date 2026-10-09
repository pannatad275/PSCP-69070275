'''cal'''
def main():
    '''cal'''
    total_cal = 0
    while True:
        choice = int(input())
        if choice == 1:
            total_cal += 100
        elif choice == 2:
            total_cal += 120
        elif choice == 3:
            total_cal += 200
        elif choice == 4:
            total_cal += 60
        elif choice == 5:
            print("Bye Bye")
            print("Total Calories:", total_cal)
            break
main()
