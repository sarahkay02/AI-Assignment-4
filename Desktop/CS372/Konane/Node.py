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
