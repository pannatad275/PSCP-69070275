'''score'''
def main():
    '''score'''
    n = int(input())
    scores = []

    for _ in range(n):
        score = int(input())
        scores.append(score)

    max_score = max(scores)
    count_max = scores.count(max_score)

    print(max_score)
    print(count_max)
main()
