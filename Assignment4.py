import random
from copy import deepcopy
from sets import Set

"""
CREATES THE NODE CLASS (to be used to represent various game states)
"""

class Node:
    def __init__(self, player, parent, board, depth, max_bool):
        self.score = 0
        self.player = player
        self.parent = parent #parent node
        self.children =[]
        self.board = board
        self.depth = depth
        self.action=[] #action this board can make
        self.max_bool = max_bool 
        self.cutoffs = 0
    
class Player:
    def __init__(self, n, player):
        self.size = n
        self.player = player

    def gen_every_move(self, board, player):
        result = Set()
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == player:
                    boardCopy = deepcopy(board)
                    result.update(self.gen_one_move(boardCopy, (i,j), player, [(i,j)]))
        print "result in gen_every_move ", result
        return result #this is a moveNode sets

    def get_node_children(self, node): #Get Children for one board and also fill all the possible actions for this node
        result = self.gen_every_move(node.board, node.player)
        if node.player == 'X':
            other_player = 'O'
        if node.player == 'O':
            other_player = 'X'

        for x in result:
            child = Node(other_player, node, x.board[:], node.depth+1, not node.max_bool)
            child.action = x.actions[:]
            child.parent = node
            node.children.append(child)
        return node.children

    def gen_one_move(self, board,(i,j), player, actions):
        move_node_set = Set()
        if player == 'X':
            other_player = 'O'
        if player == 'O':
            other_player = 'X'
        parent = MoveNode(board, None, player)
        parent.actions = actions[:]
       
        if self.valid_moves(board, (i,j), player) == []:  
            return move_node_set
        else:
            for move in self.valid_moves(board, (i,j), player):             
                move_node = MoveNode(self.next_state(board,(i,j), move, player), parent, other_player)
                move_node.actions = parent.actions[:]
                move_node.actions.append(move)
                move_node_set.add(move_node)
                move_node_set.update(self.gen_one_move(move_node.board,move_node.actions[len(move_node.actions)-1], player, move_node.actions))           
            return move_node_set


    def valid_moves(self, board, (x,y), player):
        moves=[]
        if BOARD(self.size).isValid(board, (x,y), (x-2,y), player):
            moves.append((x-2, y))
        if BOARD(self.size).isValid(board, (x,y), (x+2,y), player):
            moves.append((x+2, y))
        if BOARD(self.size).isValid(board, (x,y), (x,y-2), player):
            moves.append((x, y-2))
        if BOARD(self.size).isValid(board, (x,y), (x,y+2), player):
            moves.append((x, y+2))
        return moves

    def next_state(self, board, (x,y), (m,n), player):
        board_copy = deepcopy(board)
        if BOARD(self.size).isValid(board, (x,y), (m,n), player):
            board_copy[x][y]= ' '
            board_copy[m][n]= player
            board_copy[x+(m-x)/2][y+(n-y)/2]=' ' 
            return board_copy

    def eval_func(self, node): #evalutes the leaf Node: number of avaliable max moves - number of avaliable not max move
        if node.player == 'X':
            other_node = Node('O', node.parent, node.board, node.depth, not node.max_bool)
                
        else:
            other_node = Node('X', node.parent, node.board, node.depth, not node.max_bool)

        if node.max_bool:
            score  = len(self.get_node_children(node)) - len(self.get_node_children(other_node))
            
            while(node.parent != None):
                node = node.parent
            node.score+=1
            return score
        else:
            score= len(self.get_node_children(other_node)) - len(self.get_node_children(node))
            while(node.parent != None):
                node = node.parent
            node.score+=1
            return score

    def minimax(self, node):
        if node.depth == 4: # leaf
            return (self.eval_func(node), node.action)

        if BOARD(self.size).isLost(node.board, node.player):# this is a leafNode
            return (self.eval_func(node), node.action)

        ns = self.get_node_children(node)# children of node

        if len(ns) == 0: # leaf
            return (self.eval_func(node), node.action)

        if len(ns) == 1:#leaf = children
            return (self.eval_func(node), ns[0].action)


        if node.max_bool:
            cbv = float("-inf")
            best_move = []
            for n in ns:
                mini = self.minimax(n)
                bv = mini[0]
                move  = mini[1]
                
                if bv > cbv:
                    cbv = bv
                    bestmove = n.action[:]
            return (cbv, bestmove)
        else:
            cbv = float("inf")
            best_move = []
            for n in ns:
                mini = self.minimax(n)
                bv = mini[0]
                move = mini[1]
                
                if bv < cbv:
                    cbv = bv
                    best_move = n.action[:]
            return (cbv, best_move) 


    def minimax_alpha_beta(self, node, A, B):
        if node.depth == 4: #leaf
            return (self.eval_func(node), node.action)
        if BOARD(self.size).isLost(node.board, node.player):# leaf
            return (self.eval_func(node), node.action)
        ns = self.get_node_children(node)# children of node

        if len(ns) == 0: # leaf
            return (self.eval_func(node), node.action)

        if len(ns) == 1:# leaf = children
            return (self.eval_func(node), ns[0].action)

        if node.max_bool:
            cbv = float("-inf")
            best_move = []
            for n in ns:
                mini = self.minimax_alpha_beta(n, A, B)
                bv = mini[0]
                move  = mini[1]
                
                if bv > A:
                    A = bv
                    best_move = n.action[:]

                if A >= B:
                    n = node
                    while(n.parent != None):
                        n = n.parent
                    n.cutoffs+=1
                    return (B, best_move)
            return (A, best_move)
        else:
            cbv = float("inf")
            best_move = []
            for n in ns:
                mini = self.minimax_alpha_beta(n,A,B)
                bv = mini[0]
                move = mini[1]
                
                if bv < B:
                    B = bv
                    bestmove = n.action[:]
                if A >= B:
                    n = node
                    while(n.parent != None):
                        n = n.parent
                    n.cutoffs += 1 
                    return (A, best_move)
            return (B, best_move) 

    def read_player_moves(self, moves, board, player):
        print "moves ", moves
        p,q = moves[len(moves)-1]
        for i in range(len(moves)-1):
            x,y = moves[i]
            m,n = moves[i+1]
            board[x][y]=' '
            board[m][n]= ' '
            board[x+(m-x)/2][y+(n-y)/2]=' ' 

        board[p][q] = player
        return board


    def player_second_move(self,board):
        moves=[]
        if board[self.size-1][0]==".":
            moves.append((self.size-1,1))
            moves.append((self.size-2,0))
        elif board[0][self.size-1]==".":
            moves.append((0,self.size-2))
            moves.append((1,self.size-1))
        elif board[self.size/2-1][self.size/2]==".":
            moves.append((self.size/2-1,self.size/2+1))
            moves.append((self.size/2-1,self.size/2-1))
            moves.append((self.size/2,self.size/2))
            moves.append((self.size/2-2,self.size/2))
        elif board[self.size/2][self.size/2-1]==".":
            moves.append((self.size/2-1,self.size/2-1))
            moves.append((self.size/2+1,self.size/2-1))
            moves.append((self.size/2,self.size/2-2))
            moves.append((self.size/2,self.size/2))
        ran=random.choice(range(0,len(moves),1))
        
        inputmove=moves[ran]
        x,y=(inputmove[0],inputmove[1])
        board[x][y]="."
        return board

    def player_first_move(self,board):
        validMove=[(0,self.size-1),(self.size-1,0),(self.size/2-1,self.size/2),(self.size/2,self.size/2-1)]
        ran = random.choice(range(0,len(validMove),1))
        inputmove =validMove[ran]
        x,y=(inputmove[0],inputmove[1])
        board[x][y]="."
        return board

from sets import Set
from copy import copy, deepcopy
import random
import traceback
class BOARD:
    def __init__(self, width):
        self.width = width
        self.board = [[' ']*(self.width + 1) for row in range(self.width + 1)]

    """
    FOR BOARD FUNCTIONALITY
    """

    "Creates the 8x8 board display, using X for dark pieces and O for light pieces."
    def create_board(self):
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
    def print_board(self, board):
        for row in range(self.width + 1):
            for col in range(self.width + 1):
                print (board[row][col]),        # print on one line
            print
        print
    "Generates all possible moves."
    def gen_moves(self, board, X_or_O):
        possible_moves = []
        jump_to = (0, 0)
        up = down = left = right = 2

        for row in range(self.width + 1):
            for col in range(self.width + 1):
                "Specify whether looking for Dark/Light moves."
                if (board[row][col] == X_or_O):

                    "Can this piece move North?"
                    # current position
                    current_pos = (row, col)

                    # is move within scope of the board?
                    while ((current_pos[0] - up) > 0):
                        jump_to = (current_pos[0] - up, col)

                        # is there a blank space where we need to jump, and is there an opponent's piece to jump over?
                        if (board[jump_to[0]][jump_to[1]] == ' ' and board[jump_to[0]+1][jump_to[1]] != ' '):

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
                        if (board[jump_to[0]][jump_to[1]] == ' ' and board[jump_to[0]-1][jump_to[1]] != ' '):

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
                        if (board[jump_to[0]][jump_to[1]] == ' ' and board[jump_to[0]][jump_to[1]-1] != ' '):

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
                        if (board[jump_to[0]][jump_to[1]] == ' ' and board[jump_to[0]][jump_to[1]+1] != ' '):

                            # if so, then append this move
                            possible_moves.append((row, col, jump_to[0], jump_to[1]))

                            # update how far you'll jump next time
                            current_pos = jump_to
                        else:
                            break

        return possible_moves
    
    "Generates all possible first moves."
    def possible_first_moves(self):
        first_moves = []

        first_moves.append((1, 1))                              # top left corner
        first_moves.append((self.width/2, self.width/2))        # middle piece on left side
        first_moves.append((self.width/2+1, self.width/2+1))    # middle piece on right side
        first_moves.append((self.width, self.width))            # bottom right corner
        return first_moves

        # if (x, y) in first_moves:
        #     board[x][y] = ' '
        #     return True
        # else: 
        #     print "invalid move, please choose another piece"
        #     return False

    "Generates all possible second moves."
    def possible_second_moves(self, first_move):
        second_moves = []

        if (self.board[1][1] == ' '):
            second_moves.append((1, 2))
            second_moves.append((2, 1))

        elif (self.board[self.width][self.width] == ' '):
            second_moves.append((self.width-1, self.width))
            second_moves.append((self.width, self.width-1))

        else:
            second_moves.append((first_move[0]+1, first_move[1]))
            second_moves.append((first_move[0]-1, first_move[1]))
            second_moves.append((first_move[0], first_move[1]+1))
            second_moves.append((first_move[0], first_move[1]-1))
            
        return second_moves
        # if (x,y) in second_moves:
        #     board[x][y]=" "
        #     return True 
        # else:
        #     print "Invalid move, choose another piece."
        #     return False    
    
    def validInt(self,n):
        try:
            val = int(n)

        except ValueError:
                print("That's not an integer!Please try again.")
                return False
        return True 
    "Plays the move on the game board."
    def make_move(self, move, X_or_O):
        if (len(move) == 0):
            print "No move!"
            return 0


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
            self.print_board(self.board)
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
            self.print_board(self.board)
            return self.board


    
    def isValid(self, board, (x,y), (m,n), player):
        t=(x,y)
        h=(m,n)
        m=h[0]
        n=h[1]
        x=t[0]
        y=t[1]
        if m>=0 and m < self.width and n>=0 and n<self.width and board[m][n]=='.':
            if x>=0 and x < self.width and y>=0 and y<self.width:
                if player =='X':
                    if board[x][y]== 'X':
                        if n-y==0:
                            if abs(x-m)==2: 
                                if board[x+(m-x)/2][y+(n-y)/2]=='O':    
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        if m-x==0:
                            if abs(y-n)==2:
                                if board[x+(m-x)/2][y+(n-y)/2]=='O':    
                                    return True
                    else:
                        return False
                elif player =='O':
                    if board[x][y]=='O':
                        if n-y==0:
                            if abs(x-m)==2:
                                if board[x+(m-x)/2][y+(n-y)/2]=='X':    
                                    return True
                        if m-x==0:
                            if abs(y-n)==2:
                                if board[x+(m-x)/2][y+(n-y)/2]=='X':    
                                    return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    """
    FOR GENERATING POSSIBLE MOVES
    """


    """
    SPECIAL CASES: FIRST AND SECOND MOVES
    """

    def first_second_move(self, user_turn):
        first_moves = self.possible_first_moves()

        # if the user goes first...
        if (user_turn):
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
            self.print_board(self.board)

            # computer goes second, chooses a random legal move
            second_moves = self.possible_second_moves(coord)
            coord2 = random.choice(second_moves)

            # remove this piece from the board
            print "Computer removes " + str(coord2)
            self.board[coord2[0]][coord2[1]] = ' '
            self.print_board(self.board)

            return self.board

        # if the computer goes first...
        else:
            # choose a random legal move
            coord = random.choice(first_moves)

            # remove this piece from the board
            print "Computer removes " + str(coord)
            self.board[coord[0]][coord[1]] = ' '
            self.print_board(self.board)

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
            self.print_board(self.board)

            return self.board



    """
    FOR GETTING AND MAKING MOVES
    """

    "Asks the User for their move, or decided the best move for the Computer."
    def get_move(self, user_turn, X_or_O, possible_moves):
        # if it's the user's move...
        if (user_turn):
            # ask for user input -- needs TWO coordinates
            coordinates = input("Enter your move, in the form (x, y, x2, y2): ")

            # make sure that input is valid
            while (coordinates not in possible_moves):
                print "Error -- invalid move. Please try again."
                coordinates = input("Enter your move, in the form (x, y, x2, y2): ")

            return coordinates
        # if it's the computer's move...
        else:
            "RandomPlayer: chooses a random move out of possible legal moves."
            #best_move = random.choice(possible_moves)      # in the form (x,y) or (x, y, x2, y2)
            player=Player(self.width,'')
            # use minimax to identify the best possible move
            y = Node(player.player, None, self.board,0,True)
            #t = player.minimax_alpha_beta(y,float("-inf"),float("inf"))
            t = player.minimax(y)
            moves = t[0]
            print "number of evaluations:", y.score
            print "Player moves are ", moves
            gameBoard.board = player.read_player_moves(moves, y.board, y.player)[:]
            print gameBoard.boardToString(gameBoard.board)
            first_node = Node(self.board, None, X_or_O, None, 0, None)
            best_move = run_minimax(first_node)

            return best_move

    # def make_move(self,board, (x,y), (m,n), player):
    #     if self.isValid(board,(x,y), (m,n), player):
    #         board[x][y] = ' '
    #         board[m][n] = player
    #         board[x+(m-x)/2][y+(n-y)/2]=' '         
    #         self.boardToString(board)
    #         return board

    def isLost(self, board, player):
        if player == 'X':
            for i in range(self.width):
                for j in range(self.width):
                    if board[i][j]=='X':
                        if self.isValid(board,(i,j),(i-2,j),'X') or self.isValid(board,(i,j),(i+2,j),'X') or self.isValid(board,(i,j),(i,j-2),'X') or self.isValid(board,(i,j),(i,j+2),'X'): 
                            return False
            print player," lost"        
            return True

        if player == 'O':
            for i in range(self.width):
                for j in range(self.width):
                    if board[i][j]=='O':
                        if self.isValid(board,(i,j),(i-2,j),'O') or self.isValid(board,(i,j),(i+2,j),'O') or self.isValid(board,(i,j),(i,j-2),'O') or self.isValid(board,(i,j),(i,j+2),'O'): 
                            return False
            print player, " lost"    
            return True


class MoveNode:
    def __init__(self, board, parent, player):
        self.board = board
        self.actions =[]
        self.parent = parent
        self.player = player #after this action: parent = O, actions =[3,4], player is X but after action


    """
    MINIMAX AND STATIC EVALUATIONS
    """

    "Generates all successor nodes for a current board game state."
    def gen_successor_nodes(self, board, X_or_O, parent_node, depth_limit):
        successor_nodes = []

        # generate all possible moves for the opponent
        possible_successor_moves = self.gen_moves(board, X_or_O)

        # for each possible move...
        for move in possible_successor_moves:
            # create new board state
            current_state = deepcopy(self)
            current_state.make_move(move, X_or_O)

            # create new node
            child_node = Node(current_state.board, move, X_or_O, parent_node, parent_node.level+1, None)

            successor_nodes.append(child_node)

            # if at max level, do static evaluation and create corresponding node
            if (parent_node.level == depth_limit-1):
                child_node1 = Node(current_state.board, move, X_or_O, parent_node, parent_node.level+1, current_state.static_eval(child_node, depth_limit))

                successor_nodes.append(child_node1)

        return successor_nodes


    "Static evaluation function for possible moves."
    def static_eval(self, node, depth_limit):
        score = 0

        # whose piece is whose
        if (node.player == 'O'):
            current_player = 'X'
        else:
            current_player = 'O'

        # calculate number of our child nodes
        child_nodes = self.gen_successor_nodes(node.board, current_player, node, depth_limit)
        num_children = len(child_nodes)

        # calculate number of opponent's child nodes
        opponent_child_nodes = self.gen_successor_nodes(node.board, node.player, node, depth_limit)
        num_opponent_chidren = len(opponent_child_nodes)

        # check if
        if (num_children == 0):
            return float("-inf")

        elif (num_opponent_chidren == 0):
            return float("inf")

        else:
            # calculate score (our children - opponent's children)
            score = num_children - num_opponent_chidren

        return score


    "Minimax -- returns the best move as defined by the static evaluation function."
    def minimax(self, node, depth_limit):
        # if n is at depth limit
        if (node.level == depth_limit):
            # do a static evaluation, return result and the best move
            return (self.static_eval(node, depth_limit), node.move)

        # if n is a max node (if level is 0)
        if ((node.level % 2) == 0):
            cbv = float("-inf")

            best_move = ()

            # generate successor nodes
            successor_nodes = self.gen_successor_nodes(node.board, node.player, node, depth_limit)


            for successor in successor_nodes:
                # bv_move[0] is the static eval, bv_move[1] is the best move
                bv_move = self.minimax(successor, depth_limit)

                if bv_move[0] > cbv:
                    cbv = bv_move[0]
                    best_move = bv_move[1]

                # do a static evaluation and return the backup value
                return (cbv, best_move)

        else:
            cbv = float("inf")

            best_move = ()

            # generate successor nodes
            successor_nodes = self.gen_successor_nodes(node.board, node.player, node, depth_limit)

            for successor in successor_nodes:
                # bv_move[0] is the static eval, bv_move[1] is the best move
                bv_move = self.minimax(successor, depth_limit)

                if bv_move[0] < cbv:
                    cbv = bv_move[0]
                    best_move = bv_move[1]

                # do a static evaluation and return the backup value
                return (cbv, best_move)



"""
PLAY THE GAME
"""

def play_game(width):
    "Initialize the board game."
    board = BOARD(width)
    board.create_board()

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
    if (user_turn):
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
            # generate all possible moves for the user
            possible_moves = board.gen_moves(board.board, user_piece)

            # check if there's a winner (if no moves generates, opponent wins)
            if (possible_moves == []):
                winner = 'Computer'
                break

            # get the move from the user
            print "User's turn."
            user_move = board.get_move(user_turn, user_piece, possible_moves)

            # make move on the board
            board.make_move(user_move, user_piece)
            user_turn = False

        # if it's the computer's turn...
        else:
            # generate all possible moves for the user
            possible_moves = board.gen_moves(board.board, computer_piece)

            # check if there's a winner (if no moves generates, opponent wins)
            if (possible_moves == []):
                winner = 'User'
                break

            # get the move from the computer
            print "Computer's turn."
            computer_move = board.get_move(user_turn, computer_piece, possible_moves)

            # make move on the board
            board.make_move(computer_move, computer_piece)
            user_turn = True


    "Congratulate the winner and end the game."
    print winner + " won! Game over."


"Call the play_game() function."
play_game(8)

