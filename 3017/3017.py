'''bill'''
food_money = int(input())

SC_money1 = max(0.10 * food_money, 50.0)
SC_money2 = min(SC_money1,1000)
Total_money = (food_money + SC_money2) * 1.07

print(f"{Total_money:.2f}")