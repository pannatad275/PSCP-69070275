'''team'''
def main():
    '''team'''
    n, m = map(int, input().split())
    if not (1 <= n <= 10 and 1 <= m <= 20):
        print("Data Incorrect")
        return
    teams_data = []
    for _ in range(n):
        scores = list(map(int, input().split()))
        if len(scores) != m:
            print("Data Incorrect")
            return
        for s in scores:
            if not 0 <= s <= 100:
                print("Data Incorrect")
                return
        teams_data.append(scores)
    total_all_teams = 0
    for idx, scores in enumerate(teams_data, 1):
        team_sum = sum(scores)
        team_avg = team_sum / m
        team_max = max(scores)

        total_all_teams += team_sum

        print(f"Team {idx}: Average = {team_avg:.2f}, Max = {team_max}")

    print(f"Total Score of All Teams = {total_all_teams}")
main()
