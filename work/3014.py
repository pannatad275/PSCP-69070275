'''milk'''
def main():
    '''milk'''
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())


    cap = 0
    bottle = 0
    x = ((d // a) // b) + (d // a)


    if not b:
        bottle = d // a

    else:
        for i in range(x):
            i += 0
            if cap >= b:
                bottle += c
                cap -= b
            else:
                bottle += 1
            cap += 1

    print(bottle)
main()
