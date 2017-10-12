# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------

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

"Initialize the game board, using a multidimensional list/array."

board_size = 8      # set length of board

BOARD = {}

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


"Print the board."
def print_board(BOARD):

    for row in range(board_size + 1):
        for col in range(board_size + 1):
            print (BOARD[(row, col)]),        # print on one line
        print                                    # start a new row





print_board(BOARD)



"""
Play the game!
"""

def play():
    "Initialize the game."

    "Choose who has the first move."

    "Play the game."
