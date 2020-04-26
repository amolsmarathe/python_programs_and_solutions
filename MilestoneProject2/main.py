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

from hand import *
from account import *


def player_bet():
    while True:
        try:
            bet = int(input('What is your bet for this round? '))
        except:
            print('Enter valid bet value')
        else:
            if bet >= 10:
                break
            else:
                print('Minimum bet is 10. Please bet at least 10 or more')
                continue
    return bet


def show_cards(n, hand):
    if n == 1:
        print(f'{hand.cards[0]} is first card of {hand.name}')
    elif n == 'all':
        print(f'{hand.name}\'s cards are: ', end='')
        for i in hand.cards:
            print(f'{i} ', end='')
        print()


def is_black_jack(hand_cards):
    set_hand = set(hand_cards)
    win_set1 = {'Ace-Red', 'Ace-Black'}
    win_set2 = {'King-Red', 'King-Black', 'Queen-Red', 'Queen-Black', 'Jack-Red', 'Jack-Black', 'Ten-Red', 'Ten-Black'}
    if len(set_hand.intersection(win_set1)) == 1 and len(set_hand.intersection(win_set2)) == 1:
        return True
    else:
        return False


def player_input():
    player_choice = input('Enter your choice, HIT or STAY? ').upper()
    if player_choice != 'HIT' and player_choice != 'STAY':
        while player_choice != 'HIT' and player_choice != 'STAY':
            print('Please enter valid choice. HIT or STAY.')
            player_choice = input('Enter your choice, HIT or STAY? ').upper()
    return player_choice


def calculate_hand(hand_cards):
    hand_value = 0
    for i in hand_cards:
        hand_value += Deck.cards_with_values[i]
    return hand_value


def is_ace_in_hand(hand_cards):
    return 'Ace-Red' in hand_cards or 'Ace-Black' in hand_cards


def calculate_ace_values(hand_cards):
    aces_value = 0
    hand_value = calculate_hand(hand_cards)
    for i in hand_cards:
        if i == 'Ace-Red' or i == 'Ace-Black':
            if hand_value + 11 < 21:
                hand_value += 11
                aces_value += 11
            else:
                hand_value += 1
                aces_value += 1
    return aces_value


def check_winner():
    global player_hand_value, dealer_hand_value
    player_hand_value = calculate_ace_values(player_hand.cards) + calculate_hand(player_hand.cards)
    dealer_hand_value = calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)
    if player_hand_value > dealer_hand_value:
        return 'win'
    elif player_hand_value == dealer_hand_value:
        return 'draw'
    else:
        return 'bust'


def next_card_in_deck():
    return next(Deck.cards)


def is_bust(hand_cards):
    hand_value = calculate_ace_values(hand_cards) + calculate_hand(hand_cards)
    return hand_value > 21


def add_card_to_hand_cards(hand_cards):
    list_temp = list(hand_cards)
    list_temp.append(next_card_in_deck())
    new_hand_cards = tuple(list_temp)
    return new_hand_cards


def ask_to_continue():
    global player_account
    if player_account.balance < 10:
        'Your account balance is less than 10. You can no more play until you deposit some money.'
        return 'force_terminate'
    else:
        repeat = 'none'
        while repeat != 'Y' and repeat != 'N':
            repeat = input('Do you want to continue playing? Y/N: ').upper()
        return repeat


def is_21(hand_cards):
    hand_value = calculate_ace_values(hand_cards) + calculate_hand(hand_cards)
    return hand_value == 21


def play_hit_or_stay():
    global dealer_hand, player_hand, bet, player_account, dealer_hand_value, player_hand_value
    # Ask player if he wants to stay or hit:
    player_choice = player_input()

    # If player Stays:
    if player_choice == 'STAY':
        show_cards('all', dealer_hand)

        # Check if player lost
        if check_winner() == 'bust':
            player_account.withdraw(bet)
            print(f'Oops! You lost Rs. {bet}! Your current balance is: {player_account.balance}')
            show_cards('all', dealer_hand)
            print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')

        # If player is not yet lost or if it is a draw dealer will draw new card
        else:
            # Dealer draws more cards until he reaches 17
            while dealer_hand_value < 17:
                print('Dealer will now draw a new card for himself')
                dealer_hand.cards = add_card_to_hand_cards(dealer_hand.cards)
                dealer_hand_value = calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)
                print(f'Dealer\'s cards are now: {dealer_hand.cards} and Dealer\'s hand value is: {dealer_hand_value}')

            # Check if dealer bust:
            if dealer_hand_value > 21:
                player_account.deposit(bet*2)
                print(f'Congratulations! You have won Rs. {bet*2}! Your current balance is: {player_account.balance}')
                show_cards('all', dealer_hand)
                print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')

            # Check if dealer reaches 21
            elif dealer_hand_value == 21:
                player_account.withdraw(bet)
                print(f'Oops! You lost Rs. {bet}! Your current balance is: {player_account.balance}')
                show_cards('all', dealer_hand)
                print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')

            # If dealer is not bust or not win with 21, check if player wins/loses/draw
            else:
                if check_winner() == 'win':
                    player_account.deposit(bet*2)
                    print(f'Congratulations! You have won Rs. {bet*2}! Your current balance is: {player_account.balance}')
                    show_cards('all', dealer_hand)
                    print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')
                elif check_winner() == 'draw':
                    print(f'It was a draw! You did not lose anything. Your current balance is: {player_account.balance}')
                    show_cards('all', dealer_hand)
                    print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')
                else:
                    player_account.withdraw(bet)
                    print(f'Oops! You lost Rs. {bet}! Your current balance is: {player_account.balance}')
                    show_cards('all', dealer_hand)
                    print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')

    # If player hits:
    else:
        # Add next card to the player's hand
        player_hand.cards = add_card_to_hand_cards(player_hand.cards)

        # Check bust
        if is_bust(player_hand.cards):
            player_account.withdraw(bet)
            print(f'Oops! You lost Rs. {bet}! Your current balance is: {player_account.balance}')
            show_cards('all', player_hand)
            show_cards('all', dealer_hand)
            print(f'Your hand value was: {calculate_ace_values(player_hand.cards) + calculate_hand(player_hand.cards)}')
            print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')
        elif is_21(player_hand.cards):
            player_account.deposit(bet * 2)
            print(f'Congratulations! You have won Rs. {bet * 2}! Your current balance is: {player_account.balance}')
            show_cards('all', player_hand)
            show_cards('all', dealer_hand)
            print(f'Your hand value was: {calculate_ace_values(player_hand.cards) + calculate_hand(player_hand.cards)}')
            print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')

        else:
            show_cards('all', player_hand)
            print(f'Your current hand value is: {calculate_ace_values(player_hand.cards) + calculate_hand(player_hand.cards)}')
            play_hit_or_stay()


# Print Deck and number of cards in it (We user card_list from the Deck class and not from main because it is not yet
#           defined in main. It will be defined when game loop starts as While True)
print(Deck.card_list)
print(len(Deck.card_list))


# Set Player balance:
player_account = Account('Player', 500)


# Start a Game loop till the player is bankrupt or the player wishes to terminate

while True:

    # Shuffle the cards
    card_list = list(Deck.cards_with_values.keys()) * 2
    random.shuffle(card_list)
    Deck.cards = iter(card_list)

    # Ask player's bet and check if he has sufficient balance:
    bet = player_bet()
    while bet > player_account.balance:
        print(f'You do not have sufficient balance to place this bet. Your current balance is {player_account.balance}')
        bet = player_bet()

    # Distribute cards:
    dealer_hand = Hand('Dealer')
    player_hand = Hand('Player')

    # Show cards
    show_cards(1, dealer_hand)
    show_cards('all', player_hand)

    # Check if Black-Jack
    if is_black_jack(player_hand.cards):
        player_account.deposit(bet*3)
        print(f'Felicitations!!! You are a BLACK-JACK! You have won a jackpot of Rs. {bet*3}!'
              f'Your current balance is: {player_account.balance}')
        show_cards('all', dealer_hand)
        print(f'Dealer\'s hand value was: {calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)}')
        repeat = ask_to_continue()
        if repeat == 'force_terminate' or repeat == 'N':
            break
        else:
            continue

    else:
        # Calculate player's hand value
        player_hand_value = calculate_ace_values(player_hand.cards) + calculate_hand(player_hand.cards)
        # Display player's current Hand value
        print(f'Your current hand value is: {player_hand_value}')
        # Calculate dealer's hand value
        dealer_hand_value = calculate_ace_values(dealer_hand.cards) + calculate_hand(dealer_hand.cards)
        # Don't disclose dealer's hand value for now

    play_hit_or_stay()

    repeat = ask_to_continue()
    if repeat == 'force_terminate' or repeat == 'N':
        break
    else:
        continue


