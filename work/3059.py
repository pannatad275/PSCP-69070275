'''exam'''
def main():
    '''exam'''
    work = int(input())
    midterm = int(input())
    finalterm = int(input())
    topwork = 5
    topmidterm = 20
    topfinalterm = 25
    if work >= topwork and midterm >= topmidterm and finalterm >= topfinalterm:
        print("pass")
    else:
        print("fail")
main()
