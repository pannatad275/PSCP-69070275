'''real'''
def main():
    '''real'''
    G = int(input())
    day = int(input())
    month_limit = 1000
    count = 0
    total = 0
    for _ in range(day):
        limit = 200
        n = int(input())
        for _ in range(n):
            price = int(input())
            wepay = price *40//100
            theypay = price - wepay
            if theypay > limit:
                theypay = limit
            if theypay > month_limit:
                theypay = month_limit
            they = price - theypay
            if G >= they:
                G -= they
                limit -= theypay
                month_limit -= theypay
                total += theypay
                count += 1
    print(count)
    print(f"{G:.0f}")
    print(f"{total:.0f}")
main()
