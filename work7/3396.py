'''bad'''
N, K = map(int, input().split())
S = []
for _ in range(N):
    S.append(int(input()))

S_min = min(S)
winner_total_time = K * S_min

survivors = 0
for time_per_lap in S:
    if K == 1:
        survivors = N
        break
    time_for_k_minus_1_laps = (K - 1) * time_per_lap
    if time_for_k_minus_1_laps < winner_total_time:
        survivors += 1

print(survivors)
