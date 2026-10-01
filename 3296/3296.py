'''RGB Mixed'''
def main():
    '''r'''
    r1,g1,b1 = map(int,input().split())
    r2,g2,b2 = map(int,input().split())
    totalr = (r1 + r2) // 2
    totalg = (g1 + g2) // 2
    totalb = (b1 + b2) // 2
    print(f'{totalr} {totalg} {totalb}')
main()
