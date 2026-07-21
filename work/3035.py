'''AR tiktok'''
def main():
    '''AR tiktok'''
    x1, y1, r1 = input().split(" ")
    r = int(x1)
    x = int(y1)
    y = int(r1)

    t = x**2 + y**2
    rad = r**2

    if t < rad:
        print("IN")
    elif t == rad:
        print("ON")
    else:
        print("OUT")
main()
