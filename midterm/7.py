'''pm watch'''
def main():
    '''pm watch'''
    n = int(input())
    temp1 = int(input())
    max_temp = temp1
    if temp1 > 50:
        count_over = 1
        curr_streak = 1
        top_streak = 1
        curr_start = 1
        best_start = 1
    else:
        count_over = 0
        curr_streak = 0
        top_streak = 0
        curr_start = 0
        best_start = 0
    for day in range(2, n + 1):
        temp2 = int(input())
        if temp2 > max_temp:
            max_temp = temp2
        if temp2 > 50:
            count_over += 1
            if not curr_streak:
                curr_start = day
            curr_streak += 1
            if curr_streak >= top_streak:
                top_streak = curr_streak
                best_start = curr_start
        else:
            curr_streak = 0
            curr_start = 0
    print("OVER =", count_over)
    print("PEAK =", max_temp)
    print("STREAK =", top_streak)
    print("START =", best_start)
main()
