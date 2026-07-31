'''pro'''
import math as m
def main():
    '''pro'''
    pencil, book, colour = map(int,input().split())
    total = ((pencil * 25) + (book * 40) + (colour * 55))
    if pencil + book + colour >= 3:
        x = total * 0.90
    else:
        x = total
    print(m.floor(x))
main()
