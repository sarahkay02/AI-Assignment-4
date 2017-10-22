# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------

import sys
import random

"""
CREATES THE NODE CLASS (to be used to represent various game states)
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
FOR BOARD GAME FUNCTIONALITY
"""

"Global Variables"
blank = ' '
count_removed = 0


"Creates the 8x8 board display, using X for dark pieces and O for light pieces."
def create_board(num_rows, num_cols):
    BOARD = [[blank]*(num_cols + 1) for row in range(num_rows + 1)]

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

    return BOARD


"Choose who has the first move."
def who_first():
    first_move = random.randint(0, 1)
    if (first_move == 0):
        print "User goes first (User is Dark)."
        return 'User'
    else:
        print "Computer goes first (User is Light)."
        return 'Computer'


"Prints the board."
def print_board(BOARD):
    for row in range(num_rows + 1):
        for col in range(num_cols + 1):
            print (BOARD[row][col]),        # print on one line
            print


"Generates possible First Moves."
def first_moves(BOARD):
    first_moves = []
    first_moves.append((1, 1))                          # top left corner
    first_moves.append((num_rows/2, num_cols/2))        # middle piece on left side
    first_moves.append((num_rows/2+1, num_cols/2+1))    # middle piece on right side
    first_moves.append((num_rows, num_cols))            # bottom right corner

    return first_moves


"Generates possible Second Moves."
def second_moves(first_move, BOARD):
    second_moves = []

    if (first_move == (1, 1)):
        second_moves.append((1, 2))
        second_moves.append((2, 1))
        return second_moves

    elif (first_move == (num_rows, num_cols)):
        second_moves.append((num_rows-1, num_cols))
        second_moves.append((num_rows, num_cols-1))
        return second_moves

    else:
        second_moves.append((first_move[0]+1, first_move[1]))
        second_moves.append((first_move[0]-1, first_move[1]))
        second_moves.append((first_move[0], first_move[1]+1))
        second_moves.append((first_move[0], first_move[1]-1))
        return second_moves


"Identifies the piece(s) to remove."
def to_remove(coords):
    return False


"Removes pieces from the board."
def remove_piece(coord, BOARD):
    if (user_turn == True):
        print ("Dark removes (" + str(coord[0]) + ", " + str(coord[1]) + ")\n")
    else:
        print ("Light removes (" + str(coord[0]) + ", " + str(coord[1]) + ")\n")

    BOARD[coord[0]][coord[1]] = blank
    count_removed = count_removed + 1

    return BOARD




"""
FOR MOVES AND BASIC GAME PLAYING FUNCTIONALITY
"""

"Global Variables"
user_turn = False      # keep track of whose turn it is
winner = None       # identify the winner


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


"If user has first move".
def user_first():
    print "For the first move, only " + str(first_moves(BOARD)[0]) + ", " + str(first_moves(BOARD)[1]) + ", " + str(first_moves(BOARD)[2]) + ", or " + str(first_moves(BOARD)[3]) + " allowed."

    coord = input("Enter your move, in the form (x, y): ")

    "Make sure that user enters valid input."
    while (coord not in first_moves(BOARD)):
        print "Error -- invalid move. Please try again."
        coord = input("Enter your move, in the form (x, y): ")

    "Play the user's move on the board."
    remove_piece(coord, BOARD)

    BOARD[coord[0]][coord[1]] = blank
    print_board(BOARD)


def get_move(self, board):
    move = None
    return move


def make_move(move, board):
    return 




"""
PLAY THE GAME
"""

def playGame():
    "Initialize the board game."
    create_board(8, 8)

    "Figure out who has the first move -- if user goes first, get user input and make move on the board."
    if (who_first == 'User'):
        move = user_first()
        make_move(move, board)

    "While the game is not over..."
    while (winner == None):
        "If it's the user's turn..."
        if (user_turn == True):
            "Get the move from the user."
            move = get_move(self, board)

            "Check if there's a winner (if no moves generated, opponent wins)."
            if (move == None):
                winner = 'Computer'
                break

            "Make move on the board."
            make_move(move, board)
            user_turn == False

        "If it's the computer's turn..."
        else:
            "Get the move from the computer."
            move = get_move(self, board)

            "Check if there's a winner (if no moves generated, opponent wins)."
            if (move == None):
                winner = 'User'
                break

            "Make move on the board."
            make_move(move, board)
            user_turn = True

    "Congratulate the winner and end the game."
    print winner + "won! Game over."

