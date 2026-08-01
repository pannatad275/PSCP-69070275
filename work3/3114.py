'''airportlink'''
import math as m
def main():
    '''airportlink'''
    park_in = float(input())
    park_out = float(input())

    in_h = int(park_in)
    in_m = round((park_in - in_h) * 100)

    out_h = int(park_out)
    out_m = round((park_out - out_h) * 100)

    if not (0 <= in_h <= 24 and 0 <= in_m < 60 and 0 <= out_h <= 24 and 0 <= out_m < 60):
        print("ERROR")
        return

    if (in_h == 24 and in_m > 0) or (out_h == 24 and out_m > 0):
        print("ERROR")
        return

    time_in = in_h * 60 + in_m
    time_out = out_h * 60 + out_m

    if time_out < time_in:
        print("ERROR")
        return

    diff_m = time_out - time_in

    if diff_m <= 15:
        print("FREE")
    elif diff_m > 24 * 60:
        print("ERROR")
    else:
        hours = m.ceil(diff_m / 60)
        rates = [25, 50, 80, 110, 145, 180]
        if hours <= 6:
            price = rates[hours - 1]
        else:
            price = 250
        print(price)
main()
