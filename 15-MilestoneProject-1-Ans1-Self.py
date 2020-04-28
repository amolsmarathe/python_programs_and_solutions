
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


# ANSWER-1: (On own without any guidance, took intermittent 3 days to solve)
# Everything which is commented was done during the trial and error and all functions worked quite well :)
# Actual lines of code in this answer is 118


######################################
# Function to print the Number table for reference
######################################

def numtable():
    k = 7
    for i in range(3):

        for j in range(3):
            if j in range(2):
                print(f'{k + j}', end='|')
            else:
                print(f'{k + j}')
        k -= 3

    print()


######################################
# Print the Empty table
######################################
#
# for i in range(3):
#     if i != 2:
#         for j in range(3):
#             if j in range(2):
#                 print('_', end='|')
#             else:
#                 print('_')
#     else:
#         for j in range(3):
#             if j in range(2):
#                 print(' ', end='|')
#             else:
#                 print(' ')
#
# print()
#

######################################
# Function which takes single input and prints X in that particular position in the table.
######################################
#
# def table_print(a=0):
#     j = 7
#     for i in range(3):                  # loop for row
#         for j in range(j, j+3):         # loop for column
#             if a == j:                  # check for a (user input)
#                 print('X', end='|')
#             else:
#                 print('_', end='|')
#         print()
#         j -= 5
#

######################################
# Single player - Function which takes multiple arguments and prints X in table at those respective positions
######################################
#
#
# def table_print2(*a):
#     set1 = set(a)
#     j = 7
#     for i in range(3):                  # loop for row
#         for j in range(j, j+3):         # loop for column
#             if j in set1:               # check for 'a'- player's input
#                 print('X', end='|')
#                 set1.remove(j)
#             else:
#                 print('_', end='|')
#         print()
#         j -= 5

######################################
# 2 players - Function which takes 2 list arguments (one for each player) and prints X or 0 in table accordingly
######################################


def table_print2_modified(a, b):
    set1 = set(a)
    set2 = set(b)
    j = 7
    for i in range(3):             # loop for row
        for j in range(j, j + 3):  # loop for column
            if j in set1:          # check for a- player1 input
                print('X', end='|')
                set1.remove(j)
            elif j in set2:        # check for a- player1 input
                print('0', end='|')
                set2.remove(j)
            else:
                print('_', end='|')
        print()
        j -= 5


######################################
# Function to check if user wins during the game
######################################


def winner(current_list1):
    wincodes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
    for i in range(8):
        if set(wincodes[i]) == set(current_list1).intersection(set(wincodes[i])):
            return True
    else:
        return False


######################################
# Game loop for single player
######################################
#
#
# a = 1
# current_list1 = []
#
# while True:
#     if winner(current_list1):
#         print('You won! Bruuuuaaahhh!')
#         break
#     else:
#         x = int(input('Enter your choice of cell no.: '))
#         current_list1.append(x)
#         table_print2(*current_list1)
#         a += 1


######################################
# Functions to take user input
######################################

def player1input():
    p1 = input('Player 1- Enter the number of cell you choose: ')
    while p1 not in '123456789' or p1 == '':
        p1 = input('Invalid choice! \nPlayer 1- Again enter the number of cell you choose: ')
    else:
        return int(p1)


def player2input():
    p2 = input('Player 2- Enter the number of cell you choose: ')
    while p2 not in '123456789' or p2 == '':
        p2 = input('Invalid choice! \nPlayer 2- Again enter the number of cell you choose: ')
    else:
        return int(p2)

######################################
# Functions to modify the game board and print it with latest positions of players
######################################


def player1modifytable():
    global p1  # , player1_inputlist, player2_inputlist   --> WHY NO NEED TO DEFINE GLOBAL FUNCTIONS? WHY THERE IS ERROR
    #                 THAT GLOBAL VARIABLE NOT DEFINED AT MODULE LEVEL?
    while p1 in set(player1_inputlist).union(set(player2_inputlist)):
        print('This cell is already taken. Choose another cell.')
        p1 = player1input()
    else:
        player1_inputlist.append(p1)
        table_print2_modified(player1_inputlist, player2_inputlist)


def player2modifytable():
    global p2  # , player1_inputlist, player2_inputlist   --> WHY NO NEED TO DEFINE GLOBAL FUNCTIONS? WHY THERE IS ERROR
    #                 THAT GLOBAL VARIABLE NOT DEFINED AT MODULE LEVEL?
    while p2 in set(player1_inputlist).union(set(player2_inputlist)):
        print('This cell is already taken. Choose another cell.')
        p2 = player1input()
    else:
        player2_inputlist.append(p2)
        table_print2_modified(player1_inputlist, player2_inputlist)

######################################
# Functions to call when any of the player plays the game
######################################

def player1plays():
    global p1  # , player1_inputlist, player2_inputlist   --> WHY NO NEED TO DEFINE GLOBAL FUNCTIONS? WHY THERE IS ERROR
    #                 THAT GLOBAL VARIABLE NOT DEFINED AT MODULE LEVEL?
    p1 = player1input()
    player1modifytable()


def player2plays():
    global p2  # , player1_inputlist, player2_inputlist   --> WHY NO NEED TO DEFINE GLOBAL FUNCTIONS? WHY THERE IS ERROR
    #                 THAT GLOBAL VARIABLE NOT DEFINED AT MODULE LEVEL?
    p2 = player2input()
    player2modifytable()

######################################
# Function to check who is winner
######################################

def checkwinner():
    global winner  # , player1_inputlist, player2_inputlist   --> WHY NO NEED TO DEFINE GLOBAL FUNCTIONS? WHY THERE IS
    #                  ERROR THAT GLOBAL VARIABLE NOT DEFINED AT MODULE LEVEL?
    if winner(player1_inputlist):
        print('\nPlayer 1 Wins! Congratulations Player 1')
        return True
    elif winner(player2_inputlist):
        print('\nPlayer 2 wins! Congratulations Player 2')
        return True
    elif len((set(player1_inputlist).union(set(player2_inputlist)))) == 9:
        print('\nGame Over, no win recorded')
        return True
    else:
        return False

######################################
# Function to initialize the game and print the game information to help play the game
######################################

def initializegame():
    print(' Welcome to the GAME! /n Please have a look at the number table below. The number represents position'
          ' of the cell. Each player will enter 1 number at a time to mark his position.')
    numtable()
    print('\nPlayer 1 gets to choose "X" and Player 2 gets to choose "0". Decide amongst you who is Player 1 and'
          ' who is Player 2 and let\'s start the GAME...\n')
    return True

######################################
# Function to decide whether to continue the game
######################################


def repeat():
    while True:
        x = input('\nDo you want to play again? Y/N- ')
        if x not in 'YN' or x == '':
            print("You have entered wrong choice. Please enter 'Y' to continue playing or enter 'N' to terminate.")
            continue
        elif x == 'Y':
            print('\n'*3)
            return True
        else:
            return False


######################################
# Final Game loop for 2 players
######################################


isgameon = initializegame()

while isgameon:
    # GAME STARTS HERE--> WITH INFINITE LOOP UNTIL PLAYER CHOOSES TO STOP AFTER ANY GAME ROUND IS COMPLETE.

    player1_inputlist = []
    player2_inputlist = []

    isgameover, a = False, 1
    while isgameover == 0:
        if a % 2 != 0:
            player1plays()
        else:
            player2plays()
        isgameover = checkwinner()
        a += 1

    isgameon = repeat()
