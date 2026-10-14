'''light'''
N = int(input())
light = [False] * 360

for _ in range(N):
    A, B = map(int, input().split())

    curr = A
    while curr != B:
        light[curr] = True
        curr = (curr + 1) % 360

if all(light):
    print(360)
else:
    max_len = 0
    current_len = 0

    for i in range(720):
        if light[i % 360]:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 0

    print(max_len)
