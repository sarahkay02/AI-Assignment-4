# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------

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


class BOARD:
    def __init__(self, width, removed = 0):
        self.width = width
        self.board = [[' ']*(self.width + 1) for row in range(self.width + 1)]
        self.removed = removed


    "Creates the 8x8 board display, using X for dark pieces and O for light pieces."
    def create_board(self, width):
        for row in range(self.width + 1):
            for col in range(self.width + 1):
                # Set board's horizontal and vertical coordinate lines."
                if (row == 0):
                    self.board[row][col] = col
                    self.board[row][0] = ' '     # replace coordinate in (0,0) with a ' ' space

                elif (col == 0):
                    self.board[row][col] = row

                # Set board's alternating X's and O's.
                elif ((row + col) % 2 == 0):
                    self.board[row][col] = 'X'

                else:
                    self.board[row][col] = 'O'

        return self.board


    "Prints the board."
    def print_board(self):
        for row in range(self.width + 1):
            for col in range(self.width + 1):
                print (self.board[row][col]),        # print on one line
            print


    "Identifies the piece(s) to remove."
    def to_remove(self):

        # add code here
        return False


    "Removes pieces from the board."
    def remove_piece(self, coord, X_or_O):
        if (X_or_O == 'X'):
            print ("Dark removes (" + str(coord[0]) + ", " + str(coord[1]) + ")\n")
        else:
            print ("Light removes (" + str(coord[0]) + ", " + str(coord[1]) + ")\n")

        self.board[coord[0]][coord[1]] = ' '
        self.removed += 1

        return self.board

    """
    FOR GENERATING POSSIBLE MOVES
    """

    "Generates possible First Moves."
    def first_moves(self):
        first_moves = []
        first_moves.append((1, 1))                    # top left corner
        first_moves.append((self.width/2, self.width/2))        # middle piece on left side
        first_moves.append((self.width/2+1, self.width/2+1))    # middle piece on right side
        first_moves.append((self.width, self.width))            # bottom right corner

        return first_moves


    "Generates possible Second Moves."
    def second_moves(self, first_move):
        second_moves = []

        if (first_move == (1, 1)):
            second_moves.append((1, 2))
            second_moves.append((2, 1))
            return second_moves

        elif (first_move == (self.width, self.width)):
            second_moves.append((self.width-1, self.width))
            second_moves.append((self.width, self.width-1))
            return second_moves

        else:
            second_moves.append((first_move[0]+1, first_move[1]))
            second_moves.append((first_move[0]-1, first_move[1]))
            second_moves.append((first_move[0], first_move[1]+1))
            second_moves.append((first_move[0], first_move[1]-1))
            return second_moves


    "Helper fucntion -- checks if there is an opponent's piece ajacent to your piece."
    def opponent_ajacent(self, pos1, pos2):
        # if two coordinates are in the same row and the ajacent spot is not ' '
        if (pos1[0] == pos2[0]):
            if ((abs(pos1[1]-pos2[1])) == 1):
                return True

        # if two coordinates in the same column
        elif (pos1[1] == pos2[1]):
            if ((abs(pos1[0]-pos2[0])) == 1):
                return True
        return False



    "Generates all possible moves."
    def generate_moves(self, X_or_O):
        possible_moves = []
        jumps = []
        jump_to = (0, 0)
        up = 2
        down = 2
        left = 2
        right = 2

        for row in range(self.width + 1):
            for col in range(self.width + 1):
                "Specify whether looking for Dark/Light moves."
                if (self.board[row][col] == X_or_O):

                    # current position
                    current_pos = (row, col)

                    "Can this piece move North?"
                    up = 2

                    # is move within scope of the board?
                    while ((row - up) > 0):
                        jump_to = (row - up, col)

                        # is there an opponent's piece ajacent to this piece?
                        if (self.opponent_ajacent(current_pos, (current_pos[0], current_pos[1]+1)) == True):
                            for jump_coord in range(current_pos[1], jump_to[1]+1):
                                    jumps.append(jump_coord)
                            # is there a ' ' space where we need to jump?
                            jump_len_var = len(jumps)
                            while(jump_len_var > 0):
                                if (self.board[jump_to[0]][jump_to[1]] == ' '):
                                    possible_moves.append(((row, col), jump_to))
                                    jump_len_var -= 1

                        # update how far up you'll jump
                        current_pos = jump_to
                        up = up + 2


                    "Can this piece move South?"
                    down = 2

                    # is move within scope of the board?
                    while ((row + down) < self.width+1):
                        jump_to = (row + down, col)
                        # is there an opponent's piece ajacent to this piece?
                        if (self.opponent_ajacent(current_pos, (current_pos[0], current_pos[1]-1)) == True):
                            # is there a ' ' space where we need to jump?
                            if (self.board[jump_to[0]][jump_to[1]] == ' '):
                                possible_moves.append(((row, col), jump_to))
                                print possible_moves

                        # update how far up you'll jump
                        current_pos = jump_to
                        down = down + 2


                    "Can this piece move East?"
                    right = 2

                    # is move within scope of the board?
                    while ((col + right) < self.width+1):
                        jump_to = (row, col + right)
                        # is there an opponent's piece ajacent to this piece?
                        if (self.opponent_ajacent(current_pos, (current_pos[0]+1, current_pos[1])) == True):
                            # is there a ' ' space where we need to jump?
                            if (self.board[jump_to[0]][jump_to[1]] == ' '):
                                possible_moves.append(((row, col), jump_to))
                                print possible_moves

                        # update how far up you'll jump
                        current_pos = jump_to
                        right = right + 2


                    "Can this piece move West?"
                    left = 2

                    # is move within scope of the board?
                    while ((col - left) > 0):
                        jump_to = (row, col - left)
                        # is there an opponent's piece ajacent to this piece?
                        if (self.opponent_ajacent(current_pos, (current_pos[0]-1, current_pos[1])) == True):
                            # is there a ' ' space where we need to jump?
                            if (self.board[jump_to[0]][jump_to[1]] == ' '):
                                possible_moves.append(((row, col), jump_to))
                                print possible_moves

                        # update how far up you'll jump
                        current_pos = jump_to
                        left = left + 2

        return possible_moves




        """
        Moves only have two coordinates (just from, and to). have to figure out whether this move is legal or not. Uses the move_generator function -- is the move in there? If not, then it's not legal.
        """



    def make_move(self, move, X_or_O):
        "Understand how many jumps are being made."



        "Remove the piece(s) from the board."
        for coordinate in move:
            remove_piece(coordinate, X_or_O)

        return self.board




    "If user has first move..."
    def user_first(self):
        print "For the first move, only " + str(self.first_moves()[0]) + ", " + str(self.first_moves()[1]) + ", " + str(self.first_moves()[2]) + ", or " + str(self.first_moves()[3]) + " allowed."

        coord = input("Enter your move, in the form (x, y): ")

        "Make sure that user enters valid input."
        while (coord not in self.first_moves()):
            print "Error -- invalid move. Please try again."
            coord = input("Enter your move, in the form (x, y): ")

        "Play the user's move on the board."
        self.remove_piece(coord, 'X')

        self.print_board()





"""
FOR BASIC GAME PLAYING FUNCTIONALITY
"""

"Choose who has the first move."
def who_first():
    first_move = random.randint(0, 1)
    if (first_move == 0):
        print "User goes first (User is Dark)."
        return 'User'
    else:
        print "Computer goes first (User is Light)."
        return 'Computer'









"""
PLAY THE GAME
"""

def play_game(width):
    "Initialize the board game."
    board1 = BOARD(width)
    board1.create_board(width)

    winner = None          # identify the winner
    X_or_O = None          # keeps track of whose turn it is


    "Figure out who has the first move -- if user goes first, get user input and make move on the board."
    starting_player = who_first()

    if (starting_player == 'User'):
        board1.user_first()
        possible_moves = board1.generate_moves('X')
        print "possible_moves", possible_moves
        for move in possible_moves:
            print move





    #     make_move(move, BOARD)
    #
    # "While the game is not over..."
    # while (winner == None):
    #     # If it's the user's turn...
    #     if (user_turn == True):
    #         "Get the move from the user."
    #         move = get_move(BOARD)

    #         "Check if there's a winner (if no moves generated, opponent wins)."
    #         if (move == [] or move == "Give up"):
    #             winner = 'Computer'
    #             break
    #
    #         "Make move on the board."
    #         make_move(move, BOARD)
    #         user_turn == False
    #
    #     # If it's the computer's turn...
    #     else:
    #         "Get the move from the computer."
    #         possible_moves = generate_moves(BOARD)
    #
    #         "Check if there's a winner (if no moves generated, opponent wins)."
    #         if (possible_moves == []):
    #             winner = 'User'
    #             break
    #
    #         "Figure out the best move possible."
    #         best_move = best_move(possible_moves)
    #
    #         "Make move on the board."
    #         make_move(best_move, BOARD)
    #         user_turn = True
    #
    # "Congratulate the winner and end the game."
    # print winner + "won! Game over."





play_game(8)
