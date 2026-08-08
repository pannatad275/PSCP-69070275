'''total'''
def main():
    '''total'''
    n = int(input())
    h = []
    for _ in range(n):
        num1,num2 = int(input()),int(input())
        x = max(num1,num2)
        h.append(x)
    if n == 1:
        print(h[0])
    else:
        print(*h, sep=" + ", end=" ")
        print(f"= {sum(h)}")
main()
