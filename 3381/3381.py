'''point sorting'''
T = int(input())

for _ in range(T):
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort(key=lambda p: (p[0] + p[1], -p[1]))
    for x, y in points:
        print(f"{x} {y}")
