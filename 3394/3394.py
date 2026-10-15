'''send'''
N, S = map(int, input().split())
next_student = [0] * (N + 1)
for i in range(1, N + 1):
    next_student[i] = int(input())

visited = [False] * (N + 1)
current = S
count = 0
while current and not visited[current]:
    visited[current] = True
    count += 1
    current = next_student[current]
print(count)
