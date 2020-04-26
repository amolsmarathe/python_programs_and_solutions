"""
This module defines following methods useful to play the game in main module:
    1. request_bet - to request bet from all players
    2. ask_move - to request the player's move: Hit or Stand or Double Down
    3. is_eligible_for_double_down - to check if the player is eligible to play double down, although he wishes to to so
    4. play_game - the recursive method to play the game
    5. play_stand - method to play stand
    6. play_hit - method to play hit
    7. play_double_down - methods to play double down
    8. is_bust - method to check if the hand busted due to its value exceeding 21
    9. is_21 - method to check if the hand has value exactly 21
    10. check_win_after_dealer_draws - method to check who won after dealer draws till he reaches 17
    11. try_input_int - Error handling method to accept only particular integer as user input
    12. try_input_str - Error handling method to accept only particular string as user input
    13. ask_to_continue_playing - method to take user choice, whether to play next round or start over or quit the game
"""

from player import *
from player import Player


def request_bet(player_list):
    for player in player_list:
        player.enter_bet()
    print()
    for player in player_list:
        print(f'{player.name}\'s bet is: \n\t', player.bet)


def ask_move(player):
    while True:
        try:
            move = input(f'{player.name}, What\'s your move? Hit or Stand or Double Down? H/S/D- ')
        except Exception as e:
            print('Invalid input. Please enter Hit or Stand or Double Down.', e)
        else:
            if move[0].upper() != 'H' and move[0].upper() != 'S' and move[0].upper() != 'D':
                print('Invalid input. Please enter Hit or Stand or Double Down.')
                continue
            elif move[0].upper() == 'D':
                if is_eligible_for_double_down(player):
                    return move
                else:
                    print('You have insufficient chips balance to double your bet for playing Double Down.')
                    continue
            else:
                return move


def is_eligible_for_double_down(player):
    chips_list = list(player.bet.values)
    bet_list = list(player.bet.values)
    for i in range(4):
        if chips_list[i] <= bet_list[i]:
            return False
    else:
        return True


def play_game(player, deck):
    while True:
        move = ask_move(player)

        # Player Stands
        if move[0].upper() == 'S':
            play_stand(player)
            break

        # Player Hits
        elif move[0].upper() == 'H':
            if play_hit(player, deck) == 'end':
                break
            else:
                continue

        # Player plays Double down
        else:
            if play_double_down(player, deck) == 'end':
                break
            else:
                continue


def play_stand(player):
    player.hand.calculate_value()
    print(f'{player.name} chooses to stand with the hand value at {player.hand.value}')


def play_hit(player, deck):
    player.hand.add_card(deck)
    print(f'{player.name} has played Hit', player.hand)
    if is_bust(player):
        print(f'Oops, you busted! You lost your bet')
        player.chips.withdraw(player.bet)
        print(player.chips)
        Player.busted_or_back_jack_players.append(player)
        return 'end'
    # elif is_21(player):
    #     print(f'Congratulations {player.name} for winning this hand! You won:'
    #           f'\n{player.bet["white"] * 2} White Chips'
    #           f'\n{player.bet["red"] * 2} Red Chips'                      # No ned to check if player has 21 because
    #           f'\n{player.bet["green"] * 2} Green Chips'                    even if the player has 21, he has to wait
    #           f'\n{player.bet["black"] * 2} Black Chips')                   for dealer to draw till 17, and in that
    #     player.chips.deposit(player.bet)                                    case, there is a chance for a draw.
    #     print(player.chips)
    #     # Player.players.remove(player)
    #     return 'end'
    else:
        return 'keep_playing'


def play_double_down(player, deck):
    player.bet['white'] *= 2
    player.bet['red'] *= 2
    player.bet['green'] *= 2
    player.bet['black'] *= 2
    print(f'{player.name}, you played Double down. Your bet has been doubled now. \nYour new bet is: \n\t', player.bet)

    player.hand.add_card(deck)
    print('You have been served a new card, let us see your current position- \n', player.hand)

    if is_bust(player):
        print(f'Oops, you busted! You lost your bet')
        player.chips.withdraw(player.bet)
        print(player.chips)
        Player.busted_or_back_jack_players.append(player)
        return 'end'
    # elif is_21(player):
    #     print(f'Congratulations {player.name} for winning this hand! You won:'
    #           f'\n{player.chips.bet["white"] * 2} White Chips'
    #           f'\n{player.chips.bet["red"] * 2} Red Chips'                # No ned to check if player has 21 because
    #           f'\n{player.chips.bet["green"] * 2} Green Chips'              even if the player has 21, he has to wait
    #           f'\n{player.chips.bet["black"] * 2} Black Chips')             for dealer to draw till 17, and in that
    #     player.chips.deposit(player.bet)                                    case, there is a chance for a draw.
    #     print(player.chips)
    #     # Player.players.remove(player)
    #     return 'end'
    else:
        return 'keep_playing'


def is_bust(player):
    return player.hand.calculate_value() > 21


def is_21(player):
    return player.hand.calculate_value() == 21


def check_lost_before_dealer_draws(dealer, player_list):
    for player in player_list:
        if player.hand.calculate_value() < dealer.hand.calculate_value():
            print(f'\n{player.name}, oops you lost your bet!')
            player.chips.withdraw(player.bet)
            print(player.chips)
            Player.busted_or_back_jack_players.append(player)


def check_win_after_dealer_draws(dealer, player_list):
    if is_bust(dealer):
        print('Oops Dealer busted, players win twice their bet. Following players win:')
        for player in player_list:
            if player.hand.calculate_value() < 21:
                print(f'{player.name} is winner and wins twice the bet!')
                player.chips.deposit(player.bet)
                print(f'{player.name}, ', player.chips)

    else:
        for player in player_list:
            player_hand_value = player.hand.calculate_value()
            dealer_hand_value = dealer.hand.calculate_value()
            if 21 >= player_hand_value > dealer_hand_value:
                print(f'\n{player.name}, you win twice the bet! Congrats!')
                player.chips.deposit(player.bet)
                print(player.chips)
            elif player_hand_value < dealer_hand_value:
                print(f'\n{player.name}, oops you lost your bet!')
                player.chips.withdraw(player.bet)
                print(player.chips)
            elif player_hand_value <= 21 and player_hand_value == dealer_hand_value:
                print(f'{player.name}, it\'s a draw for this hand and you get your your bet back.')
                print(player.chips)


def check_win_when_dealer_at_17(player):
    player_hand_value = player.hand.calculate_value()
    if player_hand_value > 17:
        print(f'\n{player.name}, you win twice the bet! Congrats!')
        player.chips.deposit(player.bet)
        print(player.chips)
    elif player_hand_value < 17:
        print(f'\n{player.name}, oops you lost your bet!')
        player.chips.withdraw(player.bet)
        print(player.chips)
    elif player_hand_value <= 21 and player_hand_value == dealer_hand_value:
        print(f'{player.name}, it\'s a draw for this hand and you get your your bet back.')
        print(player.chips)


def try_input_int(input_message):
    while True:
        try:
            x = int(input(f'{input_message} '))
        except Exception as e:
            print('Please enter a valid integer.', e)
        else:
            # Place for checking condition on x
            # Can leave blank if no check required for x
            return x


def try_input_str(input_message):
    while True:
        try:
            x = input(f'{input_message} ')
        except Exception as e:
            print('Please enter a string. It cannot be empty.', e)
        else:
            # Place for checking condition on x
            # Can leave blank if no check required for x
            return x


def ask_to_continue_playing():
    while True:
        try:
            x = input('Would you like to play next round or start over a new game or quit playing? \nEnter "N" for'
                      ' next round or "S" to start over a new game or "Q" to quit playing: ')
        except Exception as e:
            print('Please enter a string. It cannot be empty.', e)
        else:
            if x[0].upper() != 'S' and x[0].upper() != 'N' and x[0].upper() != 'Q':
                print('Please enter a valid choice')
                continue
            else:
                return x[0].upper()
