'''44'''
def main():
    '''44'''
    n = input().upper()
    if len(n) == 3:
        rank = n[0] + n[1]
        group = n[2]
    else:
        rank = n[0]
        group = n[1]
    if rank == 'A':
        rank_name = 'ace'
    elif rank == 'J':
        rank_name = 'jack'
    elif rank == 'Q':
        rank_name = 'queen'
    elif rank == 'K':
        rank_name = 'king'
    else:
        rank_name = rank
    if group == 'D':
        group_name = 'diamonds'
    elif group == 'H':
        group_name = 'hearts'
    elif group == 'S':
        group_name = 'spades'
    elif group == 'C':
        group_name = 'clubs'
    else:
        group_name = ''
    print(rank_name + " of " + group_name)
main()
