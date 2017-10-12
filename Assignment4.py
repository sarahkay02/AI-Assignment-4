# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------

import random

"""
Creates the node class to be used to represent various game states.
"""

class Node:
    def __init__(self, board, move, player, level, bv):
        "Instance variables."
        self.board = board      # current board/game state
        self.move = move        # move that brought you to this state
        self.player = player    # whose move is next
        self.level = level      # node at level L in the search tree
        self.bv = bv            # backed up value, returned as a max/min

    "Class methods."
    def getBoard(self):
        return self.board

    def getMove(self):
        return self.move

    def getPlayer(self):
        return self.player

    def getLevel(self):
        return self.level

    def getBV(self):
        return self.bv



"""
Creates the 8x8 board display, using X for dark pieces and O for light pieces.
"""

"GLOBAL VARIABLES"
board_size = 8      # set length of board
BOARD = {}



"Print the board."
def print_board(BOARD):

    for row in range(board_size + 1):
        for col in range(board_size + 1):
            print (BOARD[(row, col)]),        # print on one line
        print


"Initialize the game board, using a multidimensional list/array."
def initialize_game():
    "Have every space on the board switch off with Xs and Os."
    "Also needs to include the board's coordinate lines."
    for row in range(board_size + 1):
        for col in range(board_size + 1):
            # Set board's horizontal and vertical coordinate lines."
            if (row == 0):
                BOARD[row, col] = col
                BOARD[row, 0] = ' '     # replace coordinate in (0,0) with a blank space
            elif (col == 0):
                BOARD[row, col] = row

            # Set board's X's and O's.
            elif ((row + col) % 2 == 0):
                BOARD[(row, col)] = 'X'
            else:
                BOARD[(row, col)] = 'O'

    print_board(BOARD)
    return BOARD


"Choose who has the first move."
def first_move():
    first_move = random.randint(0, 1)
    if (first_move == 0):
        print "User goes first."
    else:
        print "Computer goes first."
    return first_move

def play(BOARD):
    
    "If it's the user's move:"
    if first_move







"""
Play the game!
"""
"Initialize the game."
initialize_game()

"Choose who has the first move."
first_move()

"Play the game."
play()
