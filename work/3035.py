'''AR tiktok'''
def main():
    '''AR tiktok'''
    r, x, y = map(int,input().split())

    c = x**2 + y**2
    R = r**2
    if c < R:
        print("IN")
    elif c == R:
        print("ON")
    else:
        print("OUT")
main()
