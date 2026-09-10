'''box'''
def main():
    '''box'''
    W,L,M,N = map(int,input().split())
    total_area = W * L
    min_waste = total_area
    for i in range(M,N+1):
        used1 = W * (L // i*i)
        used2 = (L % i) * (W // i*i)
        waste = total_area -(used1 + used2)
        if waste < min_waste:
            min_waste = waste
    print(min_waste)
main()
