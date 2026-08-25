'''thaiplus fake'''
def main():
    '''thaiplus fake'''
    name = input()
    age = int(input())
    income = int(input())
    role = input()
    fam = int(input())
    if age < 18:
        print(f"{name} NOT ELIGIBLE")
        return
    if role == 'Y' or income <= 15000:
        tier = 'GOLD'
        base_amount = 3000
    elif income <= 30000:
        tier = 'SILVER'
        base_amount = 1500
    else:
        print(f"{name} NOT ELIGIBLE")
        return
    if fam >= 3:
        plus = 500
    else:
        plus = 0
    total_amount = base_amount + plus
    print(f"{name} {tier} {total_amount}")
main()
