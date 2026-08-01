'''airportlink'''
import math as m
def main():
    '''airportlink'''
    park_in = float(input()) 
    park_out = float(input())
    x = abs(park_out - park_in)
    if x <= 0.15:
        price_park = "FREE"
    else:
        x = m.ceil(x)
        if 1 <= x < 2:
            price_park = 25
        elif 2 <= x < 3:
            price_park = 50
        elif 3 <= x < 4:
            price_park = 80
        elif 4 <= x < 5:
            price_park = 110
        elif 5 <= x < 6:
            price_park = 145
        elif 6 <= x < 7:
            price_park = 180
        elif 7 <= x < 24:
            price_park = 250
        else:
            price_park = "ERROR"
    print(price_park)
main()
