# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------

import sys
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
Global Variables
"""

num_cols = num_rows = 8         # set size of board
blank = ' '

BOARD = [[blank]*(num_cols + 1) for row in range(num_rows + 1)]

user_turn = False      # keep track of whose turn it is

user_won = False       # identify the winner
computer_won = False



"""
Helper Functions
"""

"Prints the board."
def print_board(BOARD):
    for row in range(num_rows + 1):
        for col in range(num_cols + 1):
            print (BOARD[row][col]),        # print on one line
        print


"Makes sure move is legal."
def is_legal(coords):
    print "Length: ", len(coords)
    # for move in coords:
    #     # Make sure dark/light piece corresponds to user/computer
    #     if ((first_move == False and move != 'O') or (first_move == True and move != 'O')):
    #         print "Not your piece to move!"
    #         return False
    #
    #     # Make sure move is within the board and not a blank space
    #     if (move != blank) and (move[0] < 0 and move[0] > 8) and (move[1] < 0 and move[1] > 8):
    #         print "Selected piece not on the board!"
    #         return False
    #
    #     # Make sure the destination is actually available to move to
    #     while ((move+1) < len(coords)):
    #         if (move+1) != blank:
    #             print "Can't jump to this spot!"
    #             return False
    #
    #         # Make sure that the move is horizontal or vertical -- no diagonal jumps
    #     if (move[1] != x):
    #         if (y2 != y):
    #             print "Can't make diagonal jumps!"
    #             return False


        # Make sure you are actually jumping over an opponent's piece


"Identifies the piece(s) to remove."
def to_remove(coords):
    return False







"""
Play the game!
"""

"Creates the 8x8 board display, using X for dark pieces and O for light pieces."
for row in range(num_rows + 1):
    for col in range(num_cols + 1):
        # Set board's horizontal and vertical coordinate lines."
        if (row == 0):
            BOARD[row][col] = col
            BOARD[row][0] = blank     # replace coordinate in (0,0) with a blank space
        elif (col == 0):
            BOARD[row][col] = row

        # Set board's alternating X's and O's.
        elif ((row + col) % 2 == 0):
            BOARD[row][col] = 'X'
        else:
            BOARD[row][col] = 'O'


"Choose who has the first move."
def first_move():
    first_move = random.randint(0, 1)
    if (first_move == 0):
        print "User goes first (User is Dark)."
        return True
    else:
        print "Computer goes first (User is Light)."
        return False


"Start the game with whoever has the first move."
user_turn = first_move()

"""
If user has first move.
"""

"For the first move, only can choose <1, 1>, <4, 4>, <5, 5> or <8, 8>."
if (user_turn == True):
    "If user has the first turn, then prompt user for their move."
    print "For the first move, only <1, 1>, <4, 4>, <5, 5> or <8, 8> allowed."

    coord = input("Enter your move, in the form (x, y): ")

    "Make sure that user enters valid input."
    while (coord != (1, 1) and coord != (4, 4) and coord != (5, 5) and coord != (8, 8)):
        print "Error -- invalid move. Please try again."
        coord = input("Enter your move, in the form (x, y): ")

    "Play the user's move on the board."
    print ("Dark removes <" + str(coord[0]) + "," + str(coord[1]) + ">\n")

    BOARD[coord[0]][coord[1]] = blank
    print_board(BOARD)


#
#
# "While the game is not over..."
# while (winner == None):
#     "If it's the user's move..."
#     if (user_turn == True):
#         "Get the move from the user."
#         get_move()
#         play(BOARD, get_move)
#         user_turn = False
#     else:
#         "It is the computer's move."
#         get_move()
#         user_turn = True
#
#     "Create new node."
#     new_Node = Node(BOARD, -, me, 1, -infinity)
#     bv, move = minimax(new_Node)
