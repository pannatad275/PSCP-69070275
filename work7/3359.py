'''cahrm'''
def main():
    '''charm'''
    n = int(input())
    bowl_count = {}
    for _ in range(n):
        size = int(input())
        if size in bowl_count:
            bowl_count[size] += 1
        else:
            bowl_count[size] = 1
    print(max(bowl_count.values()))
main()
