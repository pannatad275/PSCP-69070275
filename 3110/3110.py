'''war'''
def main():
    '''war'''
    first,last = input().split()
    kg = float(input())
    if first == 'BKK' and last == 'CNX':
        total = 10 + (kg * 30)
    elif first == 'CNX' and last == 'UBP':
        total = 15 + (kg * 40)
    elif first == 'UBP' and last == 'BKK':
        total = 20 + (kg * 40)
    elif first == 'BKK' and last == 'PKT':
        total = 25 + (kg * 50)
    elif first == 'PKT' and last == 'CNX':
        total = 30 + (kg * 60)
    elif first == 'UBP' and last == 'PKT':
        total = 40 + (kg * 70)
    else:
        total = 0

    if total:
        print(f"{total:.2f}")
    else:
        print("Error")
main()
