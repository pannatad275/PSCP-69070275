'''score'''
def main():
    '''score'''
    bunny = int(input())
    for _ in range (bunny):
            score = int(input())
            
    max_score = max(score)
    count_max_score = score.count(max_score)
    print(max_score)
    print(count_max_score)
main()
