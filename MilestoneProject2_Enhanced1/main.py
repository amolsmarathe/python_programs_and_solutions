
# This will be the main file for the project.
# ###########################################################
# Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
#
# Here are the requirements:
#
# You need to create a simple text-based BlackJack game
# The game needs to have multiple players versus an automated dealer.
# The players can stand or hit or double down.
# The players must be able to pick their betting amount.
# You need to keep track of the player's total money.
# You need to alert the player of wins, losses, or busts, etc...
# And most importantly:
#
# You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes
# to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
# Feel free to expand this game. Try adding in Card splits!
##############################################################

"""
Structure of the game code goes as follows:

Modules: player, dealer, deck
Methods: main

"""

from dealer import *
from game_methods import *


def main():
    player_choice = 'S'
    while player_choice == 'S':

        # Set default chips balance for all players in the game
        default_chips_balance = {'white': 150, 'red': 100, 'green': 50, 'black': 20}

        # Welcome to the Casino
        print("\nWelcome everyone to the Royal Casino! You can play Black Jack and win! \n\tNOTE that every player is "
              "given certain number of chips to play with.\n\tEveryone's default chips balance at the start of the game"
              " is same, which is- \n\t", default_chips_balance)

        # Define number of players in the game and their chips balance:
        print('\nLet us now define the players for the game')
        Player.define_player_list(default_chips_balance)

        player_choice = 'N'
        while player_choice == 'N':
            # Prepare Dealer and Deck initialization
            dealer = Dealer()
            deck = Deck()
            deck.shuffle()
            print('\nThe deck is now shuffled and ready for the round')

            # Display what is everyone's chips balance:
            for player in Player.players:
                print(f'\nHey {player.name}, ', player.chips)
            print(f'Total number of players for the game are: {len(Player.players)}')

            # Dealer asks all players to bet and shows what everyone's bet is:
            request_bet(Player.players)

            # Dealer distributes cards to each player and himself
            dealer.distribute_hand(deck, Player.players)
            Player.show_details_all_players()

            # Dealer shows his second card:
            dealer.hand.show_cards('one')

            # Check if any player has Black Jack
            for player in Player.players:
                if player.hand.value == 21:
                    print(f'Congratulations {player.name}! You won a Black jack, that equals thrice your bet!!!',
                          player.chips)
                    player.chips.deposit(player.bet)
                    player.chips.deposit(player.bet)
                    print(f'{player.name}', player.chips)
                    Player.busted_or_back_jack_players.append(player)

            remaining_players_set = set(Player.players).difference(set(Player.busted_or_back_jack_players))
            remaining_players = list(remaining_players_set)

            # Continue game with remaining players:
            for player in remaining_players:
                play_game(player, deck)

            # Show Dealer's hand
            dealer.hand.show_cards('all')
            print(f'Dealer\'s hand value is: {dealer.hand.calculate_value()}')

            # Check who lost before dealer draws any card
            check_lost_before_dealer_draws(dealer, remaining_players)

            # Update the remaining players list
            remaining_players_set = set(Player.players).difference(set(Player.busted_or_back_jack_players))
            remaining_players = list(remaining_players_set)

            if len(remaining_players) != 0:

                if dealer.hand.calculate_value() < 17:

                    # Dealer draws till reaches 17
                    dealer.draw_till_17(deck)

                    # Show final dealer's hand and value
                    print('After drawing till 17, dealer\'s hand is:')
                    dealer.hand.show_cards('all')
                    print(f'Dealer\'s final hand value is: {dealer.hand.calculate_value()}')

                    # Check who wins after dealers draws till 17
                    check_win_after_dealer_draws(dealer, Player.players)
                else:
                    print('Dealer hand is at 17, no need to draw any card')
                    check_win_when_dealer_at_17(player)

                # Remove the players who have lost all their chips
            else:
                print('All players lost in this round.')
                # Ask whether to play next round or start over again with new players or quit the game
                player_choice = ask_to_continue_playing()
                if player_choice == 'N':
                    continue
                elif player_choice == 'S':
                    break
                else:
                    break


if __name__ == '__main__':
    main()
