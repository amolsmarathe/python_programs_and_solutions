# ###########################################################
# Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
#
# Here are the requirements:
#
# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the player's total money.
# You need to alert the player of wins, losses, or busts, etc...
# And most importantly:
#
# You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes
# to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
# Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits!
##############################################################

"""
Classes-
Deck -
    property: card_values (dictionary), card_list, cards (iterable)

Hand -
    property: name, cards (tuple of 2 cards)

Account -
    property: owner, balance
    method: deposit, withdraw

Functions:
    show_cards (return 2 cards, decide how many to print during runtime)
    is_black_jack
    player_input (stay or hit)
    if stay
        draw_next_card
        is_dealer17
        check_win
    else (hit)
        draw_next_card
        is_bust
        player_input (stay or hit)
        is_bust
"""

import random


class Deck:
    card_values = {'Two-Red': 2, 'Two-Black': 2, 'Three-Red': 3, 'Three-Black': 3, 'Four-Red': 4, 'Four-Black': 4,
                   'Five-Red': 5, 'Five-Black': 5, 'Six-Red': 6, 'Six-Black': 6, 'Seven-Red': 7, 'Seven-Black': 7,
                   'Eight-Red': 8, 'Eight-Black': 8, 'Nine-Red': 9, 'Nine-Black': 9, 'Ten-Red': 10, 'Ten-Black': 10,
                   'Ace-Red': 1, 'Ace-Black': 1, 'King-Red': 10, 'King-Black': 10, 'Queen-Red': 10, 'Queen-Black': 10,
                   'Jack-Red': 10, 'Jack-Black': 10}
    card_list = list(card_values.keys()) * 2
    random.shuffle(card_list)
    cards = iter(card_list)


print(Deck.card_list)
print(len(Deck.card_list))


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = next(Deck.cards), next(Deck.cards)


dealer_hand = Hand('Dealer')
player_hand = Hand('Player')
print(dealer_hand.cards, player_hand.cards)
print(dealer_hand.cards, player_hand.cards)


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


def draw_next_card():
    return next(Deck.cards)


print(draw_next_card())
