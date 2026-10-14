
'''new spe'''
rows, cols = map(int, input().split())
rabbit_r, rabbit_c = map(int, input().split())
n = int(input())
grid = [[0 for _ in range(cols)] for _ in range(rows)]
for _ in range(n):
    inf_r, inf_c = map(int, input().split())
    min_r = max(0, inf_r - 2)
    max_r = min(rows - 1, inf_r + 2)
    min_c = max(0, inf_c - 2)
    max_c = min(cols - 1, inf_c + 2)
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            dist = max(abs(r - inf_r), abs(c - inf_c))
            if not dist:
                R = 100
            elif dist == 1:
                R = 60
            elif dist == 2:
                R = 20
            else:
                R = 0
            if R > grid[r][c]:
                grid[r][c] = R
safe_count = 0
for r in range(rows):
    for c in range(cols):
        if not grid[r][c]:
            safe_count += 1
rabbit_risk = grid[rabbit_r][rabbit_c]
print(safe_count)
print(f"{rabbit_risk}%")
