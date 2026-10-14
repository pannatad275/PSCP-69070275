'''light on'''
N = int(input())
poles = []
for _ in range(N):
    poles.append(int(input()))

poles.sort()

total_distance = 0
current_pos = 0

for h in poles:
    current_pos += h
    total_distance += current_pos * 2  # ไป-กลับคูณ 2

print(total_distance)
