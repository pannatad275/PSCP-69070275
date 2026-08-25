'''pizza'''
import math
def main():
    '''pizza'''
    n = int(input())
    k = int(input())
    m = int(input())
    piece = n * k
    thad = math.ceil(piece/m)
    left = (thad * m) - piece
    print(piece)
    print(thad)
    print(left)
main()
