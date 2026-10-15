'''robot'''
first_line = input().split()
N = int(first_line[0])
P = float(first_line[1])

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

for i in range(N):
    row_tiles = sum(1 for x in grid[i] if x > 0)
    row_points = sum(grid[i])
    line_str = " ".join(map(str, grid[i]))
    print(f"{line_str} {row_tiles} {row_points}")

col_tiles = []
col_points = []
total_tiles = 0
total_points = 0

for j in range(N):
    c_tiles = 0
    c_points = 0
    for i in range(N):
        val = grid[i][j]
        c_points += val
        if val > 0:
            c_tiles += 1
    col_tiles.append(c_tiles)
    col_points.append(c_points)
    total_tiles += c_tiles
    total_points += c_points

print(" ".join(map(str, col_tiles)))
print(" ".join(map(str, col_points)))
total_fine = total_points * P
print(f"{total_tiles} {total_points} {total_fine:.2f}")
