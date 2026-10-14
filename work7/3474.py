'''resistor'''
digits = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
    "Green": 5, "Blue": 6, "Purple": 7, "Grey": 8, "White": 9
}

multipliers = {
    "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000, "Yellow": 10000,
    "Green": 100000, "Blue": 1000000, "Purple": 10000000,
    "Gold": 0.1, "Silver": 0.01
}

tolerances = {
    "Brown": 1.0, "Red": 2.0, "Green": 0.5, "Blue": 0.25,
    "Purple": 0.10, "Grey": 0.05, "Gold": 5.0, "Silver": 10.0
}

c1 = input().strip()
c2 = input().strip()
c3 = input().strip()
c4 = input().strip()

if c1 in digits and c2 in digits and c3 in multipliers and c4 in tolerances:
    base_val = (digits[c1] * 10) + digits[c2]
    r_val = base_val * multipliers[c3]

    tol = tolerances[c4] / 100.0

    lower_bound = r_val * (1.0 - tol)
    upper_bound = r_val * (1.0 + tol)

    print(f"{lower_bound:.4f}")
    print(f"{upper_bound:.4f}")
else:
    print("Error")
