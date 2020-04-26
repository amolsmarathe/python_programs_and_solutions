import random


class Deck:
    cards_with_values = {'Two-Red': 2, 'Two-Black': 2, 'Three-Red': 3, 'Three-Black': 3, 'Four-Red': 4, 'Four-Black': 4,
                         'Five-Red': 5, 'Five-Black': 5, 'Six-Red': 6, 'Six-Black': 6, 'Seven-Red': 7, 'Seven-Black': 7,
                         'Eight-Red': 8, 'Eight-Black': 8, 'Nine-Red': 9, 'Nine-Black': 9, 'Ten-Red': 10,
                         'Ten-Black': 10, 'Ace-Red': 0, 'Ace-Black': 0, 'King-Red': 10, 'King-Black': 10,
                         'Queen-Red': 10, 'Queen-Black': 10, 'Jack-Red': 10, 'Jack-Black': 10}

    card_list = list(cards_with_values.keys()) * 2
    random.shuffle(card_list)
    # cards = iter(card_list)
