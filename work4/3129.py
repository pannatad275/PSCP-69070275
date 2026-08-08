'''coffee'''
def main():
    '''coffee'''
    day = int(input())
    all_cup = []
    for _ in range(day):
        cup = int(input())
        all_cup.append(cup)
    print(sum(all_cup))
    print(max(all_cup))
    print(min(all_cup))
    print(f"{(sum(all_cup)/day):.1f}")
main()
