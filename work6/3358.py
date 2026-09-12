'''pig'''
def main():
    '''pig'''
    n = int(input())
    weights = list(map(int, input().split()))
    max_weights = []
    for i in range(0, n * 2, 2):
        w1 = weights[i]
        w2 = weights[i + 1]
        max_weights.append(max(w1, w2))
    if n == 1:
        print(max_weights[0])
    else:
        eq = " + ".join(map(str, max_weights))
        total = sum(max_weights)
        print(f"{eq} = {total}")
main()
