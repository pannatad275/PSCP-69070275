'''SurprisingVote'''
def main():
    '''SurprisingVote'''
    t_score = float(input())
    max_score = float(input())

    # t_score = max_score + (min_score / 2)
    min_score = t_score - (max_score * 2)
    if min_score < 0:
        min_score = 0
        
    if max_score - min_score >= 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
