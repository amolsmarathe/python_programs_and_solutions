"""
Player class-
    Instance variables:
        1. Name
        2. Chips (object of sub class Chips())
        3. Hand (Object of sub class Hand())
        4. Bet

    Class variable:
        1. players - list of all players who are playing the current game

    Instance Methods:
        1. show_details - for single player

    Static Methods:
        1. show_details_all_players - for all players
        2. define_player_list - to define all the players who are going to play the game

    Inner classes for Player class-
        1. Chips
            Instance variables: chips_balance (dictionary for balance per color of chips for each player)
            Instance methods: __str__ (to print current chips balance for a player)
                              deposit (to deposit winning chips into player's account)
                              withdraw (to withdraw winning chips from player's account)

        2. Hand
            Instance variables: cards (list of Card() objects in a player's hand)
                                value (hand value considering adjustment for Ace)
            Instance methods: add_card (to withdraw a card from deck and add it to the player's hand)
                              calculate_value (calculate latest hand value for the cards in the player's hand)
"""

from deck import *
from game_methods import *


class Player:
    players = []
    busted_or_back_jack_players = []

    def __init__(self, name, chips_balance_dictionary):
        self.name = name
        self.chips = Player.Chips(chips_balance_dictionary)
        self.hand = Player.Hand()
        self.bet = {'white': 0, 'red': 0, 'green': 0, 'black': 0}
        Player.players.append(self)

    def show_details(self):
        print(f'\n{self.name}\'s chips balance is:')
        print(f'\tWhite chips: {self.chips.chips_balance["white"]}, Red chips: {self.chips.chips_balance["red"]}, \n'
              f'\tGreen chips: {self.chips.chips_balance["green"]},Black chips: {self.chips.chips_balance["black"]},'
              f'\n\t  Total chips = {self.chips.chips_balance["white"] + self.chips.chips_balance["red"] + self.chips.chips_balance["green"] + self.chips.chips_balance["black"]}')
        print(f'{self.name}\'s hand is: ')
        for card in self.hand.cards:
            print(f'\t{card}')
        print(f'{self.name}\'s hand value is: {self.hand.calculate_value()}')

    @staticmethod
    def show_details_all_players():
        for player in Player.players:
            # print(f'\n{player.name}\'s chips balance is:')
            # print(f'\tWhite chips: {player.chips.chips_balance["white"]}, Red chips: {player.chips.chips_balance["red"]}, \n '
            #       f'\tGreen chips: {player.chips.chips_balance["green"]},Black chips: {player.chips.chips_balance["black"]},'
            #       f'\n\t  Total chips = {player.chips.chips_balance["white"] + player.chips.chips_balance["red"] + player.chips.chips_balance["green"] + player.chips.chips_balance["black"]}')
            print(f'{player.name}\'s hand is: ')
            for card in player.hand.cards:
                print(f'\t{card}')
            print(f'{player.name}\'s hand value is: {player.hand.calculate_value()}')
            print(f'{player.name}\'s bet is: {player.bet}')

    @staticmethod
    def define_player_list(default_chips_balance):
        count_players = try_input_int('How many players would like to play for this round? ')
        for count in range(count_players):
            name = try_input_str(f'Enter the name of player {count + 1}: ')
            Player(name, default_chips_balance)

    def enter_bet(self):
        self.bet = {'white': 0, 'red': 0, 'green': 0, 'black': 0}
        print(f'\n{self.name}, please enter your bet now:')
        for color in Player.Chips.chips_colors:
            while True:
                try:
                    chips = int(input(f'How many {color} chips would you like to bet? '))
                except Exception as e:
                    print('Please enter valid number (only integers)', e)
                else:
                    if chips <= self.chips.chips_balance[color]:
                        self.bet[color] = chips
                        break
                    else:
                        print(f'You do not have sufficient {color} chips. You have only '
                              f'{self.chips.chips_balance[color]}. Try entering correct amount if chips again')
                        continue

    class Chips:
        chips_colors = ['white', 'red', 'green', 'black']
        # chips_values = {'white': 25, 'red': 50, 'green': 100, 'black': 500}
        # Above chips values can be used for calculating the actual cost of the chips in dollars, but we have not used
        # these values in the game. Although it can be used to enhance the game experience.

        def __init__(self, chips_balance_dictionary):
            self.chips_balance = chips_balance_dictionary

        def __str__(self):
            x = '\nYour chips balance is:'
            y = f'\tWhite chips: {self.chips_balance["white"]}, Red chips: {self.chips_balance["red"]}, \n\tGreen ' \
                f'chips: {self.chips_balance["green"]},Black chips: {self.chips_balance["black"]}, \n\t  Total chip' \
                f's = ' \
                f'{self.chips_balance["white"] + self.chips_balance["red"] + self.chips_balance["green"] + self.chips_balance["black"]} '
            return x + y

        def deposit(self, chips_amount):
            self.chips_balance['white'] += chips_amount['white']
            self.chips_balance['red'] += chips_amount['red']
            self.chips_balance['green'] += chips_amount['green']
            self.chips_balance['black'] += chips_amount['black']

        def withdraw(self, chips_amount):
            self.chips_balance['white'] -= chips_amount['white']
            self.chips_balance['red'] -= chips_amount['red']
            self.chips_balance['green'] -= chips_amount['green']
            self.chips_balance['black'] -= chips_amount['black']

    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0

        def __str__(self):
            x = ''
            for card in self.cards:
                x += f'\n\t{card}'
            hand = 'Your hand is: ' + x
            value = self.calculate_value()
            hand_with_value = hand + '\nand your hand value is: ' + str(value)
            return hand_with_value

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
