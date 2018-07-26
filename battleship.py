import random

'''
# TODO: Create board class
# TODO: Create display function
# TODO: Create ship class

8x8 grid
Letters across top, numbers on side
  A  B  C  D  E  F  G  H
1 X  X  X  X  X  X  X  X
2 X  X  X  X  X  X  X  X
3 X  X  X  X  X  X  X  X
4 X  X  X  X  X  X  X  X
5 X  X  X  X  X  X  X  X
6 X  X  X  X  X  X  X  X
7 X  X  X  X  X  X  X  X
8 X  X  X  X  X  X  X  X
'''

class board(object):
    """Class for handling boards"""
    def __init__(self, size):
        super(board, self).__init__()
        self.size = size
        self.grid = []
        x = y = self.size
        for row in range(y):
            self.grid.append(list("0" * x)

    def place_ships(ships[]):
        vertical = random.choice([True, False])
        for x in ships:




def game():
    # TODO: create two boards
    # TODO: allow player to place ships
    board_size = 8
    ships = [2,3,3,4,5]
    player = board(board_size)
    enemy = board(board_size)
