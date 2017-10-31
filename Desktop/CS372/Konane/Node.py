import random
from copy import deepcopy

"""
CREATES THE NODE CLASS (to be used to represent various game states)
"""

class Node:
    def __init__(self, board, move, level):
        "Instance variables."
        self.board = board         # current board/game state
        self.move = move           # move that brought you to this state
        self.level = level         # node at level L in the search tree
