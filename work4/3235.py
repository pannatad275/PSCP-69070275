'''fat rabbit'''
def main():
    '''fat rabbit'''
    N = int(input())
    max_weight = -1
    fat_rab = ""
    count = 0
    for _ in range(N):
        NAME,KG = input().split()
        KG = int(KG)
        if KG > 15:
            count += 1
        if KG > max_weight:
            max_weight = KG
            fat_rab = NAME
    print(count)
    print(fat_rab)
main()
