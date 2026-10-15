'''bread'''
W, H, _, _ = map(int, input().split())
X = list(map(int, input().split()))
X = [0] + X + [W]

Y = list(map(int, input().split()))
Y = [0] + Y + [H]

widths = []
for i in range(len(X) - 1):
    widths.append(X[i + 1] - X[i])

heights = []
for j in range(len(Y) - 1):
    heights.append(Y[j + 1] - Y[j])

areas = []
for w in widths:
    for h in heights:
        areas.append(w * h)

areas.sort(reverse=True)
print(areas[0], areas[1])
