'''electric_using'''
def main():
    '''eu'''
    n = int(input())
    base = 0
    if n > 0:
        base += min(n,10)*5
    if n > 10:
        base += min(n-10,40)*7
    if n > 50:
        base += min(n-50,50)*10
    if n > 100:
        base += min(n-100,100)*12
    if n > 200:
        base += (n-200) * 15
    vat = round(base * 0.07, 1)
    ft = round(n * 0.50, 1)
    total = base + vat + ft
    print(f'{total:.1f}')
main()
