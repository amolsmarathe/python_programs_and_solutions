"""
Dealer class-
Instance variables:
    1. Hand (Object of sub class Hand())

Instance Methods:
    1. distribute_hand - distributes cards to start the game (2 cards per player and 2 cards to the dealer)
    2. draw_till_17 - method to draw new cards one by one to dealer until his hand reaches the value 17

Static methods:
    1. serve_one_card - serve one card to the given player from the deck

Inner classes for Dealer class-
    1. Hand
        Instance variables: cards (list of Card() objects)
                            value (hand value considering adjustment for Ace)
        Instance methods: show_cards (show the cards of the dealer, either single in the beginning or all cards at end)
                          add_card (withdraw a card from deck and add to the player's hand)
                          calculate_value (calculate latest hand value for the cards in the player's hand)
"""

from player import *


class Dealer:
    def __init__(self):
        self.hand = self.Hand()

    def distribute_hand(self, deck, players_list):
        for i in range(2):
            for player in players_list:
                player.hand.add_card(deck)
            self.hand.add_card(deck)

    def draw_till_17(self, deck):
        while self.hand.calculate_value() < 17:
            self.hand.cards.append(deck.draw_card())

    @staticmethod
    def serve_one_card(player, deck):
        print(f'\nServing one card to {player.name}')
        player.hand.add_card(deck)

    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0

        def show_cards(self, count='one'):
            if count == 'one':
                print(f'\nDealer\'s second card is: {self.cards[1]}')
            elif count == 'all':
                print(f'\nDealer\'s hand is: ')
                for card in self.cards:
                    print(f'\t{card}')

        def add_card(self, deck):
            self.cards.append(deck.draw_card())

        def calculate_value(self):
            self.value = 0
            for card in self.cards:
                self.value += Deck.card_values[card.rank]
            for card in self.cards:
                if card.rank == 'Ace':
                    if self.value + 11 > 21:
                        self.value += 1
                    else:
                        self.value += 11
            return self.value
