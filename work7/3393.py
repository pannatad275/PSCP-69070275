'''cave'''
N = int(input())
raw_cave = input().split()
cave = []
pos = 0

for i in range(N):
    val = int(raw_cave[i])
    cave.append(val)
    if val == 1:
        pos = i

commands = input()

for cmd in commands:
    new_pos = pos
    if cmd == 'L':
        new_pos = pos - 1
    elif cmd == 'R':
        new_pos = pos + 1
    if new_pos >= 0 and new_pos < N:
        pos = new_pos
        if cave[pos] == 2:
            break
ans = ""
for i in range(N):
    if i == pos:
        ans += "1"
    else:
        ans += "0"
    
    if i < N - 1:
        ans += " "

print(ans)
