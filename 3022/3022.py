'''temperature'''
def main():
    '''Temperature'''
    temp = float(input())
    unit = str(input())
    unit_w = str(input())

    if unit == "C":
        temp_unit = temp
    elif unit == "F":
        temp_unit = (temp - 32) * (5 / 9)
    elif unit == "K":
        temp_unit = temp - 273.15
    elif unit == "R":
        temp_unit = (temp * (5 / 9)) -273.15

    if unit_w == "C":
        total = temp_unit
    elif unit_w == "F":
        total = (temp_unit * (9 / 5)) + 32
    elif unit_w == "K":
        total = temp_unit + 273.15
    else:
        total = (temp_unit + 273.15) * (9 / 5)

    print(f"{total:.2f}")
main()
