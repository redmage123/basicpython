
# 1. Print out cheesy welcome

# 2. setup game data structures
x = 1
o = -1
e = 0
game = [
    [e, e, e],
    [e, e, e],
    [e, e, e],
]

# 3. Print the empty board (will require two for loops)
#     Convert value of x => 'x'
#     Convert value of o => 'o'
#     Convert value of e (empty) => '.'


# 4. Setup game loop variables
# turn, winner, and hasWon.

# 5. Game loop (while loop until someone has won):
#   print who's turn it is (X or O)
#   ask user for row (via input('prompt text'), convert to int via int(text))
#   ask user for column (same)
#   verify row and column are in bounds
#   verify that entry is not already chosen
#   set row/column to correct value (e.g. game[row][column] = x)
#   show the board again (now that it's updated)
#   check for a winner (any row or diagonal sums to 3 => x's win, -3 => o's win)
#   switch players, repeat.

# 6. Announce winner and show the winning board.
