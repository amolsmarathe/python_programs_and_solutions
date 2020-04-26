
from deck import *


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = next(Deck.cards), next(Deck.cards)

