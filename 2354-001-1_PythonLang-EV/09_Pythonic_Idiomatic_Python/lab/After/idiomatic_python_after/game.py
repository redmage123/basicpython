from board import Board

"""
Documentation for game module
"""


class Game:
    """ Documentation for Game class  """

    def __init__(self):
        """ Constructor for game. """
        self.board = Board()
        self.x = self.board.x_value
        self.o = self.board.o_value
        self.active_player = self.x

    @property
    def has_winner(self):
        """Returns True if there a winner, else False."""
        return not self.find_winner() is None

    @property
    def current_player_name(self):
        """The name of the current player (X or O)"""
        return "X" if self.active_player == self.x else "O"

    @property
    def winner(self):
        """Returns X or O if there is a winner"""
        if not self.has_winner:
            return "No winner"

        return "X" if self.find_winner() == self.x else "O"

    def find_winner(self):
        """Computes that current game checking for a winner."""
        board = self.board
        winner = None
        c = board.cells
        for i in range(3):

            sums = [
                c[0][0] + c[0][1] + c[0][2],  # row 1
                c[1][0] + c[1][1] + c[1][2],  # row 2
                c[2][0] + c[2][1] + c[2][2],  # row 3
                c[0][0] + c[1][0] + c[2][0],  # col 1
                c[0][1] + c[1][1] + c[2][1],  # col 2
                c[0][2] + c[1][2] + c[2][2],  # col 3
                c[0][0] + c[1][1] + c[2][2],  # diagonal 1
                c[0][2] + c[1][1] + c[2][0]  # diagonal 2
            ]
            if 3 in sums:
                winner = "X"

            if -3 in sums:
                winner = "O"

        return winner

    def cell_already_played(self, row, col):
        """Checks whether a cell has been played"""
        return not self.board.cells[row][col] == self.board.empty

    def get_cell(self, row, col):
        """Gets the value of a cell."""
        return self.board.cells[row][col]

    def play_cell(self, row, col):
        """Places the current player's symbol in that cell."""
        self.board.cells[row][col] = self.active_player

    def switch_players(self):
        """Cycles the current player."""
        self.active_player = self.x if self.active_player == self.o else self.o

