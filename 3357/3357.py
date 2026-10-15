'''giraffe'''
N = int(input())
giraffes = []
for _ in range(N):
    giraffes.append(int(input()))
if N == 1:
    print(1)
else:
    count = 0
    for i in range(N):
        if not i:
            if giraffes[0] > giraffes[1]:
                count += 1
        elif i == N - 1:
            if giraffes[N - 1] > giraffes[N - 2]:
                count += 1
        else:
            if giraffes[i] > giraffes[i - 1] and giraffes[i] > giraffes[i + 1]:
                count += 1

    print(count)
