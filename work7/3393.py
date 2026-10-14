'''cave'''
def main():
    '''cave'''
    n = int(input())
    cave = list(map(int, input().split()))
    commands = input().strip()

    pos = cave.index(1)

    for cmd in commands:
        new_pos = pos
        if cmd == 'R':
            new_pos += 1
        elif cmd == 'L':
            new_pos -= 1

        if 0 <= new_pos < n:
            pos = new_pos
            if cave[pos] == 2:
                break

    final_cave = [0] * n
    for i in range(n):
        if cave[i] == 2 and i != pos:
            final_cave[i] = 2

    final_cave[pos] = 1

    print(*final_cave)
main()