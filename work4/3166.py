'''exam'''
def main():
    '''exam'''
    n = int(input())
    scores = []
    for _ in range(n):
        score = int(input())
        scores.append(score)
    x = sum(scores) / n
    if x >= 60 and min(scores) >= 50:
        print(f"{x:.1f}")
        print("PASS")
    else:
        print(f"{x:.1f}")
        print("FAIL")
main()
