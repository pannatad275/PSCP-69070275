'''ramen'''
def main():
    '''ramen'''
    size, Type = input().split()
    price_s = 0
    if Type == "R":
        if size == "S":
            price_s = 60
        elif size == "M":
            price_s = 80
        elif size == "L":
            price_s = 100
    elif Type == "T":
        if size == "S":
            price_s = 80
        elif size == "M":
            price_s = 100
        elif size == "L":
            price_s = 120
    top_line2 = input().split()
    topping = top_line2[0]
    if topping == "N":
        price_t = 0
        piece = 0
    else:
        piece = int(top_line2[1])
        if topping == "P":
            price_t = 15
        else:
            price_t = 10
    total_t = price_t * piece
    ans = total_t + price_s
    print(ans)
main()
