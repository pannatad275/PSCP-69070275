'''inflation'''
def main():
    '''inflation'''
    n = float(input())
    k = int(input())
    satang = int(n * 100 + 0.5)
    for _ in range(k):
        increase = (satang * 381) // 10000
        satang += increase
    baht = satang // 100
    rem = satang % 100
    if rem < 10:
        print(str(baht) + ".0" + str(rem))
    else:
        print(str(baht) + "." + str(rem))
main()
