'''in the line'''
N, _ = map(int, input().split())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

max_prefix = [0] * N
current_max = 0
for i in range(N):
    if H[i] > current_max:
        current_max = H[i]
    max_prefix[i] = current_max

for pos in A:
    idx = pos - 1
    if not idx:
        print(0)
    else:
        max_in_front = max_prefix[idx - 1]
        if H[idx] > max_in_front:
            print(0)
        else:
            print(max_in_front - H[idx] + 1)
