
# Problem Statement:
#
# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
#
# Here are the requirements:
#
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
#

# ANSWER-2:
# This Answer2 follows the solution given in Udemy course, however, I was not able to add error condition check when
# user input is not 1-9 ad some string or space or just enter. This can be achieved using exception handling but
# it was not in the scope of this milestone project


import random


def display_board_and_num_pad(board):
    print(board[7] + '|' + board[8] + '|' + board[9] + '   ' * 4 + '7' + '|' + '8' + '|' + '9')
    print(board[4] + '|' + board[5] + '|' + board[6] + '   ' * 4 + '4' + '|' + '5' + '|' + '6')
    print(board[1] + '|' + board[2] + '|' + board[3] + '   ' * 4 + '1' + '|' + '2' + '|' + '3')


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_marker():
    marker = ''
    while marker not in 'XO' or marker == '':
        marker = input("Player 1, Select your marker 'X' or 'O': ").upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def flip():
    turn = random.randint(1, 2)
    if turn == 1:
        print('Player 1 starts first')
    else:
        print('Player 2 starts first')
    return turn


def is_position_available(board, position):
    return board[position] == ' '


def ask_player_input(board):
    position = 0
    while position not in range(1, 10) or position == '' or is_position_available(board, position) == False:
        position = int(input('Enter player1 position: '))

    return position


def check_winner(board, marker):
    win_codes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in range(8):
        if board[win_codes[i][0]] == board[win_codes[i][1]] == board[win_codes[i][2]] == marker:
            return True
    else:
        return False


def is_board_full(board):
    return ' ' not in board[1:10]


def player1_plays(board, player1_marker):
    # Display current board
    display_board(board)
    # Take player input
    position = ask_player_input(board)
    # Update the board with position
    board[position] = player1_marker


def player2_plays(board, player2_marker):
    # Display current board
    display_board(board)
    # Take player input
    position = ask_player_input(board)
    # Update the board with position
    board[position] = player2_marker


def is_game_on():
    repeat = input('Do you want to play again? Y/N: ').upper()
    while repeat not in 'YN':
        repeat = input('Enter correct choice Y/N \nDo you want to play again? Y/N: ').upper()
    return repeat == 'Y'
# Game begins:

# Display Test Board
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board_and_num_pad(test_board)

print('\nWelcome to Tic Tac Toe game\n')

# Infinite Game loop starts - will end until user chooses to stop playing.
game_on = True
while game_on:

    # make the board Empty
    board = [' '] * 10

    # Take player marker
    player1_marker, player2_marker = player_marker()
    print(f'Player 1 marker is {player1_marker} and Player 2 marker is {player2_marker}')

    # Who starts first?
    turn = flip()

    while True:
        # Player 1 plays
        if turn == 1:
            player1_plays(board, player1_marker)
            # Check winner
            if check_winner(board, player1_marker):
                display_board(board)
                print('Player 1 wins!')
                break
            elif is_board_full(board):
                display_board(board)
                print('Game Tie!')
                break
            else:
                turn = 2

        # Player 2 plays
        else:
            player2_plays(board, player2_marker)
            # Check winner
            if check_winner(board, player2_marker):
                display_board(board)
                print('Player 2 wins!')
                break
            elif is_board_full(board):
                display_board(board)
                print('Game Tie!')
                break
            else:
                turn = 1

    game_on = is_game_on()
