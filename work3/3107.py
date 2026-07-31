'''Bonus'''
def main():
    '''Bonus'''
    role, age, money = input().split()
    age = float(age)
    money = float(money)
    x = 0
    percent_bonus = 0
    if role == 'M':
        x = 1500
        if age < 5:
            percent_bonus = 0.06
        elif age <= 10:
            percent_bonus = 0.08
        else:
            percent_bonus = 0.10

    elif role == 'B':
        x = 1000
        if age < 5:
            percent_bonus = 0.05
        elif age <= 10:
            percent_bonus = 0.06
        else:
            percent_bonus = 0.07

    elif role == 'G':
        x = 500
        if age < 5:
            percent_bonus = 0.04
        elif age <= 10:
            percent_bonus = 0.05
        else:
            percent_bonus = 0.06
    total_bonus = x + (money * percent_bonus)
    print(f"{total_bonus:.0f}")
main()
