'''school'''
def main():
    '''school'''
    role = input()
    n = int(input())
    total = []
    for _ in range(n):
        price = float(input())
        total.append(price)
    if role == "Y":
        x = sum(total)
        total_pay = x * 0.95
    else:
        x = sum(total)
        if x >= 500:
            total_pay = x * 0.97
        else:
            total_pay = x
    ans = round(total_pay + 1e-9,2)
    print(f"{ans:.2f}")
main()
