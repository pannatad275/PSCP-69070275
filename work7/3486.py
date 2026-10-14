'''bullet'''
N = int(input())

shots = []
for _ in range(N):
    x, y, d = map(int, input().split())
    shots.append((x, y, d))

F = False
for Tx in range(1001):
    for Ty in range(1001):
        if all((Tx - x)**2 + (Ty - y)**2 == d**2 for x, y, d in shots):
            print(f"{Tx} {Ty}")
            break
    if F:
        break
