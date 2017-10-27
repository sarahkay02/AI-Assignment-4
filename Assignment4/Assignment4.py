# Assignment4.py
# Lizzie Siegle and Sujin Kay

# Implements a program to play the game of Konane (Hawaiian Checkers).
# ---------------------------------------------------------------------------

import random

"""
CREATES THE NODE CLASS (to be used to represent various game states)
"""
class Node:
    def __init__(self, player, parent, board, level, max_bool):
        "Instance variables."
        self.player = player # whose move is next
        self.parent = parent #node
        self.board = board         # current board/game state      
        self.level = level         # node at level L in the search tree
        self.moves = [] #moves the board can make
        self.max_bool = max_bool 
        self.score = 0
        self.children =[]

class NodeToMove:
    def __init__(self, board, parent, player):
        self.board = board
        self.moves_arr=[]
        self.parent = parent
        self.player = player 

class BOARD:
    def __init__(self, width, num_removed = 0):
        self.width = width
        self.board = [[' ']*(self.width + 1) for row in range(self.width + 1)]
        self.num_removed = num_removed

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


    "Identifies the piece(s) to remove."
    def to_remove(self):

        # add code here
        return False


    "Removes pieces from the board."
    def remove_piece(self, coord, X_or_O):
        if (X_or_O == 'X'):
            print ("Dark removes " + str(coord) + "\n")
        else:
            print ("Light removes " + str(coord) + "\n")

        self.board[coord[0]][coord[1]] = ' '
        self.num_removed += 1

        return self.board

    # def check_leaf(self, node): #evaluates leaf: num avail max moves - num avail !max moves
    #     if node.player == 'X':
    #         comp_node = Node('O', node.parent, node.board, node.level, not node.max_bool)
                
    #     else:
    #         comp_node = Node('X', node.parent, node.board,node.level, not node.max_bool)

    #     if node.max_bool:
    #         score  = len(self.get_children_of_node(node)) - len(self.get_children_of_node(comp_node))
            
    #         while(node.parent != None):
    #             node = node.parent
    #         node.score += 1
    #         return score
    #     else:
    #         score = len(self.get_children_of_node(comp_node)) - len(self.get_children_of_node(node))
    #         while(node.parent != None):
    #             node = node.parent
    #         node.score += 1
    #         return score

    def get_children_of_node(self, node): #Get children for board, fill all possible moves of node
        possible_moves = self.generate_moves(node.player)
        if node.player == 'X':
            children_player = 'O'
        if node.player == 'O':
            children_player = 'X'

        for r in possible_moves:
            print ("node ", node)
            print("r in result ", r)
            child = Node(children_player, node, node.board, r.level+1, not node.max_bool)
            child.moves = r.moves_arr[:]
            child.parent = node
            node.children.append(child)
        return node.children

    def minimax(self, node):
        if node.level == 3: #leaf
            return (self.check_leaf(node), node.moves) #return e(n), move(n)

        # if BOARD(self.width).check_loss(node.board, node.player): #leaf
        #     return (self.check_leaf(node), node.moves)

        # expand n to n1, n2...nb successors
        ns = self.get_children_of_node(node) #all children of node

        # if len(ns) == 0: #leaf 
        #     return (self.check_leaf(node), node.moves)

        # if len(ns) == 1: #children = leaf
        #     return (self.check_leaf(node), ns[0].moves)


        if node.max_bool:
            cbv = float("-inf")
            best_move = []
            for n in ns:
                bv = self.minimax(n)
                move  = self.minimax(n)
                if bv > cbv:
                    cbv = bv
                    best_move = move #n.moves[:]
            return (cbv,best_move)
        else: #min node
            cbv = float("inf") # + infinity 
            best_move = []
            for n in ns: #loop through node in successors
                bv = self.minimax(n) #back value
                move = self.minimax(n) #move
                if bv < cbv:
                    cbv = bv
                    best_move = move #n.moves[:]
            return (cbv,best_move)

    def minimax_alpha_beta(self, node, alpha, beta):
        if node.level == 6: #leaf
            return (self.check_leaf(node), node.moves)
        if BOARD(self.width).check_loss(node.currentBoard, node.moves): # leaf
            return (self.check_leaf(node), node.moves)

        ns = self.getChildrenForANode(node) #all node children
        if len(ns) == 0: #leaf
            return (self.check_leaf(node), node.moves)
        if len(ns) == 1: #children = leaf
            return (self.check_leaf(node), ns[0].moves)
        if node.max_bool:
            cbv = float("-inf")
            best_move = []

            for n in ns: #loop through children
                mmab = self.minimax_alpha_beta(n, alpha, beta)
                bv = mmab[0] #back value
                move  = t[1]
            
                if bv > alpha:
                    alpha = bv
                    best_move = n.moves[:]

                if alpha >= beta:
                    return (beta, best_move)
            return (alpha,bestmove)

        else:
            cbv = float("inf")
            best_move = []
            for n in ns:
                t = self.minimax_alpha_beta(n, alpha, beta)
                bv = t[0]
                move = t[1]
            
                if bv < beta:
                    beta = bv
                best_move = n.moves[:]
                if alpha >= beta:
                    return (alpha, best_move)
            return (B,bestmove)


    """
    FOR GENERATING POSSIBLE MOVES
    """

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
        jump_to = (0, 0)
        up = down = left = right = 2

        # if it's the first move...
        if (self.num_removed == 0):
            possible_moves.append((1, 1))                              # top left corner
            possible_moves.append((self.width/2, self.width/2))        # middle piece on left side
            possible_moves.append((self.width/2+1, self.width/2+1))    # middle piece on right side
            possible_moves.append((self.width, self.width))            # bottom right corner

            return possible_moves

        # if it's the second move...
        elif (self.num_removed == 1):
            if (self.board[1][1] == ' '):
                possible_moves.append((1, 2))
                possible_moves.append((2, 1))
                return possible_moves

            elif (self.board[self.width][self.width] == ' '):
                possible_moves.append((self.width-1, self.width))
                possible_moves.append((self.width, self.width-1))
                return possible_moves

            elif (self.board[self.width/2][self.width/2]):
                possible_moves.append((self.width/2+1, self.width/2))
                possible_moves.append((self.width/2-1, self.width/2))
                possible_moves.append((self.width/2, self.width/2+1))
                possible_moves.append((self.width/2, self.width/2-1))
                return possible_moves

            else:
                possible_moves.append((self.width/2+2, self.width/2+1))
                possible_moves.append((self.width/2, self.width/2+1))
                possible_moves.append((self.width/2+1, self.width/2+2))
                possible_moves.append((self.width/2+1, self.width/2))
                return possible_moves

        else:
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

                            # is there an opponent's piece ajacent to this piece?
                            if (self.opponent_ajacent(current_pos, (current_pos[0]-1, current_pos[1])) == True):
                                # is there a ' ' space where we need to jump?
                                if (self.board[jump_to[0]][jump_to[1]] == ' '):
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
                            # is there an opponent's piece ajacent to this piece?
                            if (self.opponent_ajacent(current_pos, (current_pos[0]+1, current_pos[1])) == True):
                                # is there a ' ' space where we need to jump?
                                if (self.board[jump_to[0]][jump_to[1]] == ' '):
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
                            # is there an opponent's piece ajacent to this piece?
                            if (self.opponent_ajacent(current_pos, (current_pos[0], current_pos[1]+1)) == True):
                                # is there a ' ' space where we need to jump?
                                if (self.board[jump_to[0]][jump_to[1]] == ' '):
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
                            # is there an opponent's piece ajacent to this piece?
                            if (self.opponent_ajacent(current_pos, (current_pos[0], current_pos[1]-1)) == True):
                                # is there a ' ' space where we need to jump?
                                if (self.board[jump_to[0]][jump_to[1]] == ' '):
                                    # if so, then append this move
                                    possible_moves.append((row, col, jump_to[0], jump_to[1]))

                                    # update how far you'll jump next time
                                    current_pos = jump_to
                                else:
                                    break
            return possible_moves



    """
    FOR GETTING AND MAKING MOVES
    """

    "Asks the User for their move, or decided the best move for the Computer."
    def get_move(self, user_turn, possible_moves):
        # if it's the user's move...
        if (user_turn == True):
            # regular case (normal game play)
            if (self.num_removed > 1):
                # ask for user input -- needs TWO coordinates
                coordinates = input("Enter your move, in the form (x, y, x2, y2): ")

                # make sure that input is valid
                while (coordinates not in possible_moves):
                    print "Error -- invalid move. Please try again."
                    coordinates = input("Enter your move, in the form (x, y, x2, y2): ")

                return coordinates


            # special cases
            else:
                # if it's the first move...
                if (self.num_removed == 0):
                    # give instructions
                    print "For the first move, only " + str(possible_moves[0]) + ", " + str(possible_moves[1]) + ", " + str(possible_moves[2]) + ", or " + str(possible_moves[3]) + " allowed."
                else:
                    print "For the second move, can only remove a piece ajacent to first move."

                # ask for user input
                coord = input("Enter your move, in the form (x, y): ")

                # make sure that input is valid
                while (coord not in possible_moves):
                    print "Error -- invalid move. Please try again."
                    coord = input("Enter your move, in the form (x, y): ")

                return coord


        # if it's the computer's move...
        else:
            best_move = ()      # in the form (x,y) or ((x,y), (x2,y2))
            # use minimax and alphabeta pruning to identify the best possible move

            """
            CODE HERE
            """
            minimax_node = Node("O", None, self.board, 0, True)
            best_move = self.minimax(minimax_node)

            return best_move

    def is_legal(self, board, (x,y), (i,j), player):
        move1 = (x,y)
        move2 = (i,j)
        i = move2[0]
        j = move2[1]
        x = move1[0]
        y = move1[1]
        if i >= 0 and j < self.width-1 and j >= 0 and j < self.width-1 and board[i][j] == ' ':
            if x >= 0 and x < self.width-1 and y >= 0 and y < self.width-1:
                if player =='X':
                    if board[x][y]== 'X':
                        if j - y == 0:
                            if abs(x-i) == 2: 
                                if board[x+(i-x)/2][y+(j-y)/2] == 'O':          
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        if i - x == 0:
                            if abs(y-j) == 2:
                                if board[x+(i-x)/2][y+(j-y)/2] == 'O':    
                                    return True
                                else:
                                    return False
            elif player =='O':
                if board[x][y] == 'O':
                    if j-y == 0:
                        if abs(x-i) == 2:
                            if board[x+(i-x)/2][y+(j-y)/2] =='X':    
                                return True
                    if i-x == 0:
                        if abs(y-j) == 2:
                            if board[x+(i-x)/2][y+(j-y)/2] =='X':    
                                return True
                            else:
                                return False
        else:
            return False

    def check_loss(self, board, player):
        if player == "X":
            for i in range(self.width-1):
                for j in range(self.width-1):
                    if board[i][j]=='X':
                        if self.is_legal(board,(i,j),(i-2,j),'X') or self.is_legal(board,(i,j),(i+2,j),'X') or self.is_legal(board,(i,j),(i,j-2),'X') or self.is_legal(board,(i,j),(i,j+2),'X'): 
                            return False
            print player, " didn\'t win"        
            return True

        if player == 'O':
            for i in range(self.width-1):
                for j in range(self.width-1):
                    if board[i][j]=='O':
                        if self.is_legal(board,(i,j),(i-2,j),'O') or self.is_legal(board,(i,j),(i+2,j),'O') or self.is_legal(board,(i,j),(i,j-2),'O') or self.is_legal(board,(i,j),(i,j+2),'O'): 
                            return False
            print player," didn\'t win"    
            return True



    def make_move(self, move, X_or_O):
        print "move:", move
        # if the 'move' is just to remove a piece (one coordinate)
        if (len(move) == 2):
            self.remove_piece(move, X_or_O)
            self.print_board()
            return self.board

        # if the 'move' is a jump (or multiple jumps)
        else:
            """
            CODE HERE
            """

            self.print_board()
            return self.board




"""
OTHER FUNCTIONS
"""







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


    "Start playing!"
    # while the game is not over...
    while (winner == None):
        # if it's ithe user's turn...
        if (user_turn == True):
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