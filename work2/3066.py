'''same'''
def main():
    '''same'''
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    if n1 == n2 and n1== n3:
        x = "all the same"
    elif n1 != n2 and n1 != n3 and n2 != n3:
        x = "all different"
    else:
        x = "neither"
    print(x)
main()
