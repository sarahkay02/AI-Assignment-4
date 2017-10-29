# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------
import random
from sets import Set
from copy import copy, deepcopy
import traceback

"""
CREATES THE NODE CLASS (to be used to represent various game states)
"""
class MoveNode:
    def __init__(self,board,parent, player):
        self.board = board
        self.moves_list = []
        self.parent = parent
        self.player = player 


class Node():
    def __init__(self, player, parent, board, depth, max_bool):
        self.score = 0
        self.player = player
        self.parent = parent #parent node
        self.children =[]
        self.board = board
        self.depth = depth
        self.moves = [] # move board can make
        self.max_bool = max_bool #true if max


class BOARD:
    def __init__(self, width, num_removed = 0):
        self.width = width
        self.board = [[' ']*(self.width + 1) for row in range(self.width + 1)]
        self.num_removed = num_removed

    def set_moves(self, board, player):
        result = Set()
        for i in range(self.width):
            for j in range(self.width):
                if board[i][j] == player:
                    result.update(self.one_move(board,(i,j), player,[(i,j)]))
        return result #this is a moveNode sets

    def one_move(self, board,(i,j),player,moves):
        move_nodes = Set()
        if player == 'X':
            other = 'O'
        if player == 'O':
            other = 'X'
        parent = MoveNode(board, None, player)
        parent.moves = moves[:]
        if self.generate_moves(player) == []:  
            return move_nodes
        else:
            for move in self.generate_moves(player):             
                move_node = MoveNode(self.next_state(board,(i,j),move,player), parent, other)
                move_node.moves_list = parent.moves_list[:]
                move_node.moves_list.append(move)
                move_nodes.add(move_node)
                move_nodes.update(self.one_move(move_node.board, move_node.moves_list[len(move_node.moves_list)-1], player, move_node.moves_list))           
            return move_nodes

    def get_children(self, node): #Get children for one board and also fill all the possible actions for this node
        result = self.set_moves(node.board, node.player)
        if node.player == 'X':
            other_player = 'O'
        if node.player == 'O':
            other_player = 'X'

        for x in result:
            child = Node(other_player, node,x.board[:], node.depth+1, not node.isMax)
            child.moves = x.moves_list[:]
            child.parent = node
            node.children.append(child)
        return node.children

    def check_valid(self,(x,y), (m,n), player):
        t = (x,y)
        h = (m,n)
        m = h[0]
        n = h[1]
        x = t[0]
        y = t[1]
        if m >= 0 and m < self.width and n >= 0 and n < self.width and self.board[m][n] == ' ':
            if x >= 0 and x < self.width and y >= 0 and y < self.width:
                if player == 'X':
                    if self.board[x][y] == 'X':
                        if n-y == 0:
                            if abs(x-m) == 2: 
                                if self.board[x+(m-x)/2][y+(n-y)/2] == 'O':     
                                    return True #valid
                                else:
                                    return False #should pick move with'0' in between
                            else: 
                                return False #should pick move with'0' in between
                        if m-x==0:
                            if abs(y-n)==2:
                                if self.board[x+(m-x)/2][y+(n-y)/2]=='O':    
                                    return True #valid
                    else:
                        return False #pick x
                elif player =='O':
                    if self.board[x][y]=='O':
                        if n-y==0:
                            if abs(x-m)==2:
                                if self.board[x+(m-x)/2][y+(n-y)/2]=='X':    
                                    return True
                        if m-x==0:
                            if abs(y-n)==2:
                                if self.board[x+(m-x)/2][y+(n-y)/2]=='X':    
                                    return True
                    else:
                        return False #pick 0
            else:
                return False #invalid
        else:
            return False #invalid

    def next_state(self, board, (x,y), (m,n), player):
        board2 = deepcopy(board)
        if Konane(self.size).isValid(board,(x,y),(m,n),player):
            board2[x][y]= ' '
            board2[m][n]= player
            board2[x+(m-x)/2][y+(n-y)/2]='.' 
            return board2

    def eval_leaf(self, node): #evaluates leaf: num of avail max moves - num avail not max moves
        if node.player == 'X':
            other_node = Node('O', node.parent, node.currentBoard,node.depth, not node.max_bool)              
        else:
            other_node = Node('X', node.parent, node.board, node.depth, not node.max_bool)

        if node.max_bool:
            score  = len(self.get_children(node)) - len(self.get_children(other_node))
            
            while(node.parent!=None):
                node = node.parent
            node.score= node.score+1
            return score
        else:
            score = len(self.get_children(other_node)) - len(self.get_children(node))
            while(node.parent!=None):
                node = node.parent
            node.score += 1
            return score

    def minimax(self, node):
        if node.depth==3: #is a leaf
            return (self.eval_leaf(node), node.moves)

        ns = self.get_children(node) #all children of node

        if len(ns) == 0: # leaf
            return (self.eval_leaf(node), node.moves)

        if len(ns) == 1: # children = leaf
            return (self.eval_leaf(node), ns[0].moves)


        if node.max_bool:
            cbv = float("-inf")
            best_move = []
            for n in ns:
                t = self.minimax(n)
                bv = t[0]
                move  = t[1]
                
                if bv > cbv:
                    cbv = bv
                    best_move = n.moves[:]
                    
            return (cbv,best_move)
        else:
            cbv = float("inf")
            best_move = []
            for n in ns:
                t = self.minimax(n)
                bv = t[0]
                move = t[1]
                
                if bv < cbv:
                    cbv = bv
                    best_move = n.moves[:]
            return (cbv,best_move)

    """
    FOR BOARD FUNCTIONALITY
    """

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
        print




    """
    FOR GENERATING POSSIBLE MOVES
    """

    "Generates all possible first moves."
    def possible_first_moves(self):
        first_moves = []

        first_moves.append((1, 1))                              # top left corner
        first_moves.append((self.width/2, self.width/2))        # middle piece on left side
        first_moves.append((self.width/2+1, self.width/2+1))    # middle piece on right side
        first_moves.append((self.width, self.width))            # bottom right corner

        return first_moves


    "Generates all possible second moves."
    def possible_second_moves(self, first_move):
        second_moves = []

        if (self.board[1][1] == ' '):
            second_moves.append((1, 2))
            second_moves.append((2, 1))
            return second_moves

        elif (self.board[self.width][self.width] == ' '):
            second_moves.append((self.width-1, self.width))
            second_moves.append((self.width, self.width-1))
            return second_moves

        else:
            second_moves.append((first_move[0]+1, first_move[1]))
            second_moves.append((first_move[0]-1, first_move[1]))
            second_moves.append((first_move[0], first_move[1]+1))
            second_moves.append((first_move[0], first_move[1]-1))
            return second_moves


    def generate_moves(self, X_or_O):
        possible_moves = []
        jump_to = (0, 0)
        up = down = left = right = 2

        for row in range(self.width + 1):
            for col in range(self.width + 1):
                "Specify whether looking for Dark/Light moves."
                if (self.board[row][col] == X_or_O):

                    "Can this piece move North?"
                    # current position
                    current_pos = (row, col)

                    # is move within scope of the board?
                    while ((current_pos[0] - up) > 0):
                        jump_to = (current_pos[0] - up, col)

                        # is there a blank space where we need to jump, and is there an opponent's piece to jump over?
                        if (self.board[jump_to[0]][jump_to[1]] == ' ' and self.board[jump_to[0]+1][jump_to[1]] != ' '):

                            # if so, then append this move
                            possible_moves.append((row, col, jump_to[0], jump_to[1]))

                            # update how far you'll jump next time
                            current_pos = jump_to
                        else:
                            break


                    "Can this piece move South?"
                    # current position
                    current_pos = (row, col)

                    # is move within scope of the board?
                    while ((current_pos[0] + down) < self.width+1):
                        jump_to = (current_pos[0] + down, col)

                        # is there a blank space where we need to jump, and is there an opponent's piece to jump over?
                        if (self.board[jump_to[0]][jump_to[1]] == ' ' and self.board[jump_to[0]-1][jump_to[1]] != ' '):

                            # if so, then append this move
                            possible_moves.append((row, col, jump_to[0], jump_to[1]))

                            # update how far you'll jump next time
                            current_pos = jump_to
                        else:
                            break


                    "Can this piece move East?"
                    # current position
                    current_pos = (row, col)

                    # is move within scope of the board?
                    while ((current_pos[1] + right) < self.width+1):
                        jump_to = (row, current_pos[1] + right)

                        # is there a blank space where we need to jump, and is there an opponent's piece to jump over?
                        if (self.board[jump_to[0]][jump_to[1]] == ' ' and self.board[jump_to[0]][jump_to[1]-1] != ' '):

                            # if so, then append this move
                            possible_moves.append((row, col, jump_to[0], jump_to[1]))

                            # update how far you'll jump next time
                            current_pos = jump_to
                        else:
                            break


                    "Can this piece move West?"
                    # current position
                    current_pos = (row, col)

                    # is move within scope of the board?
                    while ((current_pos[1] - left) > 0):
                        jump_to = (row, current_pos[1] - left)

                        # is there a blank space where we need to jump, and is there an opponent's piece to jump over?
                        if (self.board[jump_to[0]][jump_to[1]] == ' ' and self.board[jump_to[0]][jump_to[1]+1] != ' '):

                            # if so, then append this move
                            possible_moves.append((row, col, jump_to[0], jump_to[1]))

                            # update how far you'll jump next time
                            current_pos = jump_to
                        else:
                            break

        return possible_moves


    """
    SPECIAL CASES: FIRST AND SECOND MOVES
    """

    def first_second_move(self, user_turn):
        first_moves = self.possible_first_moves()

        # if the user goes first...
        if (user_turn == True):
            # give instructions
            print "For the first move, only " + str(first_moves[0]) + ", " + str(first_moves[1]) + ", " + str(first_moves[2]) + ", or " + str(first_moves[3]) + " allowed."

            # ask for user input
            coord = input("Enter your move, in the form (x, y): ")

            # make sure that input is valid
            while (coord not in first_moves):
                print "Error -- invalid move. Please try again."
                coord = input("Enter your move, in the form (x, y): ")

            # remove this piece from the board
            print "User removes " + str(coord)
            self.board[coord[0]][coord[1]] = ' '
            self.print_board()

            # computer goes second, chooses a random legal move
            second_moves = self.possible_second_moves(coord)
            coord2 = random.choice(second_moves)

            # remove this piece from the board
            print "Computer removes " + str(coord2)
            self.board[coord2[0]][coord2[1]] = ' '
            self.print_board()

            return self.board

        # if the computer goes first...
        else:
            # choose a random legal move
            coord = random.choice(first_moves)

            # remove this piece from the board
            print "Computer removes " + str(coord)
            self.board[coord[0]][coord[1]] = ' '
            self.print_board()

            # give user instructions
            second_moves = self.possible_second_moves(coord)
            print "For the second move, can only remove a piece ajacent to first move."

            # ask for user input
            coord2 = input("Enter your move, in the form (x, y): ")

            # make sure that input is valid
            while (coord2 not in second_moves):
                print "Error -- invalid move. Please try again."
                coord2 = input("Enter your move, in the form (x, y): ")

            # remove this piece from the board
            print "User removes " + str(coord2)
            self.board[coord2[0]][coord2[1]] = ' '
            self.print_board()

            return self.board



    """
    FOR GETTING AND MAKING MOVES
    """

    "Asks the User for their move, or decided the best move for the Computer."
    def get_move(self, user_turn, possible_moves):
        # if it's the user's move...
        if (user_turn == True):
            # ask for user input -- needs TWO coordinates
            coordinates = input("Enter your move, in the form (x, y, x2, y2): ")

            # make sure that input is valid
            while (coordinates not in possible_moves):
                print "Error -- invalid move. Please try again."
                coordinates = input("Enter your move, in the form (x, y, x2, y2): ")
            return coordinates
        # if it's the computer's move...
        else:
            best_move = random.choice(possible_moves)      # in the form (x,y) or (x, y, x2, y2)
            # use minimax and alphabeta pruning to identify the best possible move
            """
            CODE HERE
            """
            y = Node('O',None,self.board,0,True)
            #t = robot.minimaxAB(y,float("-inf"),float("inf"))
            t = self.minimax(y)
            moves = t[1]
            print(t[1])
            return t[1]


    def make_move(self, move, X_or_O):
        if (X_or_O == 'X'):
            print "Dark moves (" + str(move[0]) + ", " + str(move[1]) + ") to (" + str(move[2]) + ", " + str(move[3]) + ")"
        else:
            print "Light moves (" + str(move[0]) + ", " + str(move[1]) + ") to (" + str(move[2]) + ", " + str(move[3]) + ")"


        # if the move is horizontal (coordinates are in the same row)
        if (move[0] == move[2]):
            # remove your original piece
            self.board[move[0]][move[1]] = ' '

            # each time you jump, remove the opponent's piece that youre jumping over
            current_col = move[1]

            # if you're going East...
            if (move[3] > move[1]):
                while (current_col < move[3]):
                    # remove the opponent's piece from the board
                    self.board[move[0]][current_col+1] = ' '
                    current_col += 2

            # if you're going West...
            else:
                while (current_col > move[3]):
                    # remove the opponent's piece from the board
                    self.board[move[0]][current_col-1] = ' '
                    current_col -= 2

            # insert your jumping piece to the final spot
            self.board[move[2]][move[3]] = X_or_O
            self.print_board()
            return self.board

        # if the move is vertical (coordinates are in the same column)
        else:
            # remove your original piece
            self.board[move[0]][move[1]] = ' '

            # each time you jump, remove the opponent's piece that youre jumping over
            current_row = move[0]

            # if you're going North...
            if (move[0] > move[2]):
                while (current_row > move[2]):
                    # remove the opponent's piece from the board
                    self.board[current_row-1][move[1]] = ' '
                    current_row -= 2

            # if you're going South...
            else :
                while (current_row < move[2]):
                    # remove the opponent's piece from the board
                    self.board[current_row+1][move[1]] = ' '
                    current_row += 2

            self.board[move[2]][move[3]] = X_or_O
            self.print_board()
            return self.board



"""
PLAY THE GAME
"""

def play_game(width):
    "Initialize the board game."
    board = BOARD(width)
    board.create_board(width)

    winner = None                # identifies the winner
    user_piece = None            # is User X or O?
    computer_piece = None        # is Computer X or O?
    user_turn = None             # keeps track of whose turn it is


    "Decide who goes first."
    who_first = raw_input("Who goes first? (Enter 'User' or 'Computer'): ")

    if (who_first == 'User'):
        print "User goes first (User is 'X', Computer is 'O')."
        user_piece = 'X'
        computer_piece = 'O'
        user_turn = True

    else:
        print "Computer goes first (Computer is 'X', User is 'O')."
        user_piece = 'O'
        computer_piece = 'X'
        user_turn = False


    "Play the first and second moves."
    if (user_turn == True):
        board.first_second_move(user_turn)
        user_turn = True

    else:
        board.first_second_move(user_turn)
        user_turn = False


    "Start playing!"
    # while the game is not over...
    while (winner == None):
        # if it's the user's turn...
        if (user_turn == True):
            print "User's turn."

            # generate all possible moves for the user
            possible_moves = board.generate_moves(user_piece)

            # check if there's a winner (if no moves generates, opponent wins)
            if (possible_moves == []):
                winner = 'Computer'
                break

            # get the move from the user
            user_move = board.get_move(user_turn, possible_moves)

            # make move on the board
            board.make_move(user_move, user_piece)
            user_turn = False

        # if it's the computer's turn...
        else:
            print "Computer's turn."

            # generate all possible moves for the user
            possible_moves = board.generate_moves(computer_piece)

            # check if there's a winner (if no moves generates, opponent wins)
            if (possible_moves == []):
                winner = 'User'
                break

            # get the move from the computer
            computer_move = board.get_move(user_turn, possible_moves)

            # make move on the board
            board.make_move(computer_move, computer_piece)
            user_turn = True


    "Congratulate the winner and end the game."
    print winner + " won! Game over."


"Call the play_game() function."
play_game(8)