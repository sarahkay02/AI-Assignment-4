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




"GLOBAL VARIABLES."
board_size = 8         # set length of board
BOARD = {}

user_turn = False      # keep track of whose turn it is

user_won = False       # identify the winner
computer_won = False


"Helper function -- prints the board."
def print_board(BOARD):
    for row in range(board_size + 1):
        for col in range(board_size + 1):
            print (BOARD[(row, col)]),        # print on one line
        print



"""
Play the game!
"""

"Creates the 8x8 board display, using X for dark pieces and O for light pieces."
for row in range(board_size + 1):
    for col in range(board_size + 1):
        # Set board's horizontal and vertical coordinate lines."
        if (row == 0):
            BOARD[row, col] = col
            BOARD[row, 0] = ' '     # replace coordinate in (0,0) with a blank space
        elif (col == 0):
            BOARD[row, col] = row

        # Set board's alternating X's and O's.
        elif ((row + col) % 2 == 0):
            BOARD[(row, col)] = 'X'
        else:
            BOARD[(row, col)] = 'O'


"Choose who has the first move."
def first_move():
    first_move = random.randint(0, 1)
    if (first_move == 0):
        print "User goes first."
        return True
    else:
        print "Computer goes first."
        return False


"Start the game with whoever has the first move."
user_turn = first_move()

"While the game is not over..."
while (winner == None):
    "If it's the user's move..."
    if (user_turn == True):
        "Get the move from the user."
        get_move()
        play(BOARD, get_move)
        user_turn = False
    else:
        "It is the computer's move."
        get_move()
        user_turn = True

    "Create new node."
    new_Node = Node(BOARD, -, me, 1, -infinity)
    bv, move = minimax(new_Node)
