import random
from copy import deepcopy

"""
CREATES THE NODE CLASS (to be used to represent various game states)
"""

class Node:
    def __init__(self, board, move, level, depth_limit, player, who_first):
        "Instance variables."
        self.board = board         # current board/game state
        self.move = move           # move that brought you to this state
        self.level = level         # node at level L in the search tree
        self.depth_limit = depth_limit          # depth limit for searching
        self.player = player
        self.who_first = who_first








def multijump():
    for successor in successor_nodes:
        if successor.move[0] == successor.move[2]:
            if (abs(successor.move[1]-successor.move[3])) > 2:
                best_move = successor.move
                return (float("inf"), best_move)

        # if move in the same row
        else:
            if (abs(successor.move[0]-successor.move[2])) > 2:
                best_move = successor.move
                return(float("inf"), best_move)
