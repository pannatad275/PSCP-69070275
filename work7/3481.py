'''l'''
def main():
    '''dw'''
    l, n = map(int, input().split())
    bridges = []
    for _ in range(n):
        a, b = map(int, input().split())
        bridges.append((a, b))

    max_bridges = 0

    for i in range(l):
        x = i + 0.5
        count = 0
        for a, b in bridges:
            if a < x < b:
                count += 1

        if count > max_bridges:
            max_bridges = count

    print(max_bridges)
main()
