'''Pro'''
def main():
    '''pro'''
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())

    if z >= x:
        people_inpro = (z // x) * y
        people_notpro = z % x
        price = a
        X = (people_inpro + people_notpro) * price
        print(X)
    else:
        print(a * z)
main()
