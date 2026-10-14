'''card'''
def main():
    '''card'''
    card_code = input().upper()

    ranks = {
        'A': 'Ace',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King'
    }

    suits = {
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades',
        'C': 'Clubs'
    }

    rank_part = card_code[:-1]
    suit_part = card_code[-1]

    rank_name = ranks.get(rank_part, rank_part)

    suit_name = suits.get(suit_part, "")

    print(f"{rank_name} of {suit_name}")
main()
