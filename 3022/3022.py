'''Temperature'''
temp = float(input())
u = str(input())
uw = str(input())

if u == "C":
    temp_unit = temp
elif u == "F":
    temp_unit = (temp - 32) * (5 / 9)
elif u == "K":
    temp_unit = temp - 273.15
elif u == "R":
    temp_unit = (temp * (5 / 9)) -273.15

if uw == "C":
    total = temp_unit
elif uw == "F":
    total = (temp_unit * (9 / 5)) + 32
elif uw == "K":
    total = temp_unit + 273.15
elif uw == "R":
    total = (temp_unit + 273.15) * (9 / 5)

print(f"{total:.2f}")
