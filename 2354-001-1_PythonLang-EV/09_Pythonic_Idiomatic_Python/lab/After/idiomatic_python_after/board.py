""" Defines the Board class. """


class Board(object):
    """Represents the state of a board in a game of tic-tac-toe"""

    def __init__(self):
        """Creates an empty Board"""
        self.x_value = 1
        self.o_value = -1
        self.empty = 0
        self.cells = self.build_empty_board()

    def build_empty_board(self):
        """Builds an empty board"""
        cells = [
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
        ]
        return cells

    def print_board(self):
        """Prints the board to the console."""
        for row in self.cells:
            for cell_value in row:
                print('x' if cell_value == self.x_value else
                      ('o' if cell_value == self.o_value else '.'), end=' ')
            print()

    def __str__(self):
        text = ""
        for row in self.cells:
            for cell_val in row:
                text += ('x' if cell_val == self.x_value else
                         ('o' if cell_val == self.o_value else '.'))
            text += "\n"
        return text
